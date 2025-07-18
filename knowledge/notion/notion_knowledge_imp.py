import os
from knowledge.knowledge_service import KnowledgeService
from handlers.metadata_handler import metadata_handler
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.document.base import Document as AgnoDocument
from agno.embedder.google import GeminiEmbedder
from typing import List, Optional
from langchain_community.document_loaders import NotionDBLoader
from langchain_core.documents.base import Document
from utils.logger.logger import log_message

class NotionKnowledgeImp(KnowledgeService):
    _instance: Optional[KnowledgeService] = None
    _documents: Optional[List[Document]] = None
    _vector_db: Optional[ChromaDb] = None
    knowledge_base: Optional[DocumentKnowledgeBase] = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self) -> None:
        super().__init__()
        log_message("NotionKnowledgeImp initialized", "INFO")

    async def initialize(self) -> None:
        """Initialize the knowledge service."""
        await self._load_data()
        await self._process_data()

    async def _load_data(self) -> None:
        """Load data from Notion."""
        try:
            token = os.getenv("NOTION_TOKEN")
            id = os.getenv("NOTION_ID")
            if not token or not id:
                raise ValueError("NOTION_TOKEN and NOTION_ID environment variables must be set.")
            loader = NotionDBLoader(integration_token=token, database_id=id, request_timeout_sec=30)
            self._documents = loader.load()
            if not self._documents:
                raise ValueError("No documents found in the Notion database.")
            log_message(f"Loaded {len(self._documents)} documents from Notion.", "DEBUG")
        except ValueError as e:
            log_message(f"Error loading Notion data: {e}", "ERROR")
            return
        finally:
            log_message("Finished loading Notion data.", "SUCCESS")

    async def _process_data(self) -> None:
        """Process the loaded Notion data."""
        try:
            self._vector_db = ChromaDb(
                collection="notion_knowledge_base",
                path="./vector_db/notion_knowledge_base",
                persistent_client=True,
                embedder=GeminiEmbedder(),
            )
            agno_documents: list[AgnoDocument] = []
            if not self._documents:
                raise ValueError("No documents to process.")
            for doc in self._documents:
                cleaned_meta = {}
                if doc.metadata:
                    cleaned_meta = metadata_handler(doc.metadata)
                    agno_doc = AgnoDocument(
                        id=doc.id,
                        content=doc.page_content,
                        meta_data=cleaned_meta
                    )
                    agno_documents.append(agno_doc)
            self.knowledge_base = DocumentKnowledgeBase(vector_db=self._vector_db, documents=agno_documents)
            self.knowledge_base.load(recreate=False)
        except Exception as e:
            log_message(f"Error processing Notion data: {e}", "ERROR")
        finally:
            log_message("Finished processing Notion data.", "SUCCESS")
            
    async def reload_data(self) -> None:
        """Reload the data from the source."""
        pass
    
    async def close(self) -> None:
        """Close the knowledge service."""
        pass