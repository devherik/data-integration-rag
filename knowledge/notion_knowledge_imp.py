from knowledge.knowledge_service import KnowledgeService
import os
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.document.chunking.fixed import FixedSizeChunking
from agno.document.base import Document as AgnoDocument
from agno.embedder.google import GeminiEmbedder
from typing import Optional
from langchain_community.document_loaders import NotionDBLoader
from langchain_core.documents.base import Document

class NotionKnowledgeImp(KnowledgeService):
    _instance: Optional[KnowledgeService] = None
    knowledge_base: Optional[DocumentKnowledgeBase] = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        print("Initializing NotionKnowledgeImp")
        super().__init__()
        print("NotionKnowledgeImp initialized")

    async def _load_data(self) -> None:
        """Load data from Notion."""
        pass

    async def _process_data(self) -> None:
        """Process the loaded Notion data."""
        pass