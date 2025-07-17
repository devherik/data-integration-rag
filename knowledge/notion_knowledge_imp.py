import os
from knowledge.knowledge_service import KnowledgeService
from handlers.metadata_handler import metadata_handler
from agno.knowledge.document import DocumentKnowledgeBase
from agno.vectordb.chroma import ChromaDb
from agno.document.chunking.fixed import FixedSizeChunking
from agno.document.base import Document as AgnoDocument
from agno.embedder.google import GeminiEmbedder
from typing import List, Optional
from langchain_community.document_loaders import NotionDBLoader
from langchain_core.documents.base import Document

# Define ANSI escape codes for colors and reset
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'  # Resets all formatting

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
        print(f"{BLUE}INFO {RESET}NotionKnowledgeImp initialized{RESET}")

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
            print(f"{GREEN}SUCCESS {RESET}Loaded {len(self._documents)} documents from Notion.{RESET}")
        except ValueError as e:
            print(f"{RED}ERROR {RESET}Error loading Notion data: {e}{RESET}")
            return
        finally:
            print(f"{GREEN}SUCCESS {RESET}Finished loading Notion data.{RESET}")

    async def _process_data(self) -> None:
        """Process the loaded Notion data."""
        try:
            self._vector_db = ChromaDb(
                collection="notion_knowledge_base",
                path="./vector_db/notion_knowledge_base",
                embedding_model=GeminiEmbedder(),
                chunking_strategy=FixedSizeChunking(chunk_size=512, overlap=50)
            )
            agno_documents: list[AgnoDocument] = metadata_handler(documents=self._documents if self._documents is not None else [])
            self.knowledge_base = DocumentKnowledgeBase(vector_db=self._vector_db, documents=agno_documents)
            self.knowledge_base.load(recreate=False)
        except Exception as e:
            print(f"{RED}ERROR {RESET}Error processing Notion data: {e}{RESET}")
        finally:
            print(f"{GREEN}SUCCESS {RESET}Finished processing Notion data.{RESET}")