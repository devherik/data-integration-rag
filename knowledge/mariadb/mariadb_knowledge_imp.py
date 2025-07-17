import os
from knowledge.knowledge_service import KnowledgeService
from typing import Optional, List, Any
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from sqlalchemy import Connection, Engine, create_engine, text, CursorResult
from urllib.parse import quote_plus

from utils.logger.logger import log_message

class MariaDBKnowledgeImp(KnowledgeService):
    _instance: Optional[KnowledgeService] = None
    _engine: Optional[Engine] = None
    _db_connection: Optional[Connection] = None
    _documents: Optional[CursorResult[Any]] = None
    _vector_db: Optional[ChromaDb] = None
    knowledge_base: Optional[DocumentKnowledgeBase] = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        super().__init__()
        log_message("MariaDBKnowledgeImp initialized", "INFO")

    async def initialize(self) -> None:
        """Initialize the knowledge service."""
        try:
            host = os.getenv("MARIADB_HOST", "localhost")
            port = os.getenv("MARIADB_PORT", "3306")
            user = os.getenv("MARIADB_USER", "root")
            password = quote_plus(os.getenv("MARIADB_PASSWORD", "your_password"))
            engine_path = f"mariadb+mariadbconnector://{user}:{password}@{host}:{port}/rci"
            self._engine = create_engine(engine_path)
            self._db_connection = self._engine.connect()
            log_message("MariaDB engine created successfully.", "SUCCESS")
        except Exception as e:
            log_message(f"Error creating MariaDB engine: {e}", "ERROR")
            return
        await self._load_data()
        await self._process_data()
    
    async def _load_data(self) -> None:
        """Load data from the source."""
        if not self._db_connection:
            return
        try:
            self._documents = self._db_connection.execute(text("SELECT * FROM tb_rci"))
            for row in self._documents:
                log_message(f"Row: {row}", "DEBUG")
        except Exception as e:
            log_message(f"Error loading data into MariaDB: {e}", "ERROR")

    async def _process_data(self) -> None:
        """Process the loaded documents."""
        pass
    
    async def reload_data(self) -> None:
        """Reload the data from the source."""
        pass
    
    async def close(self) -> None:
        """Close the knowledge service."""
        try:
            if self._db_connection:
                self._db_connection.close()
                log_message("MariaDB connection closed successfully.", "SUCCESS")
        except Exception as e:
            log_message(f"Error closing MariaDB connection: {e}", "ERROR")