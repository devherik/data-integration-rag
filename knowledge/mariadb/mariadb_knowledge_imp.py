import os
from handlers.database_data_handler import databaseDataHandler
from knowledge.knowledge_service import KnowledgeService
from typing import Optional, List, Any
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.document.base import Document as AgnoDocument
from agno.embedder.google import GeminiEmbedder
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
            log_message(f"Loaded {self._documents.rowcount} documents from MariaDB.", "DEBUG")
        except Exception as e:
            log_message(f"Error loading data into MariaDB: {e}", "ERROR")

    async def _process_data(self) -> None:
        """Process the loaded documents."""
        try:
            self._vector_db = ChromaDb(
                collection="mariadb_knowledge_base",
                path="./vector_db/mariadb_knowledge_base",
                persistent_client=True,
                embedder=GeminiEmbedder(),
            )
            agno_documents: list[AgnoDocument] = []
            if not self._documents:
                raise ValueError("No documents to process.")
            for row in self._documents.mappings():
                # Process the row to create a clean metadata dictionary.
                raw_metadata = databaseDataHandler(row.items())
                # Filter out None values, as the vector database does not support them.
                metadata = {k: v for k, v in raw_metadata.items() if v is not None}

                # Generate a unique ID from the metadata, falling back to a default.
                # Ensure your databaseDataHandler provides a consistent 'ID' key.
                doc_id = str(
                    metadata.get("ID", f"unknown_id_{row.get('id', 'no_pk')}")
                    or metadata.get("id", f"unknown_id_{row.get('id', 'no_pk')}")
                )

                # Create a structured string representation of the row for the content.
                # This format can improve search and embedding quality.
                content = ", ".join([f"{key}: {value}" for key, value in row.items() if value is not None])

                # Create the AgnoDocument instance.
                agno_doc = AgnoDocument(
                    id=doc_id,
                    content=content,
                    meta_data=metadata
                )
                agno_documents.append(agno_doc)
            self.knowledge_base = DocumentKnowledgeBase(vector_db=self._vector_db, documents=agno_documents)
            self.knowledge_base.load(recreate=False)
        except Exception as e:
            log_message(f"Error processing MariaDB data: {e}", "ERROR")
            return
        finally:
            log_message("Finished processing MariaDB data.", "SUCCESS")
    
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