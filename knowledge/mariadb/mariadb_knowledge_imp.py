import os
from knowledge.knowledge_service import KnowledgeService
from typing import Optional, List
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.chroma import ChromaDb

from utils.logger.logger import log_message

class MariaDBKnowledgeImp(KnowledgeService):
    _instance: Optional[KnowledgeService] = None
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
        await self._load_data()
        await self._process_data()
    
    async def _load_data(self) -> None:
        """Load data from the source."""
        pass
    
    async def _process_data(self) -> None:
        """Process the loaded documents."""
        pass
    
    async def reload_data(self) -> None:
        """Reload the data from the source."""
        pass