import os
import asyncio
from dotenv import load_dotenv
from knowledge.notion.notion_knowledge_imp import NotionKnowledgeImp
from utils.logger.logger import log_message

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_path):
    load_dotenv(env_path)
else:
    log_message(f".env file not found at {env_path}", "WARNING")

async def main():
    notion_knowledge = NotionKnowledgeImp()
    await notion_knowledge.initialize()

if __name__ == "__main__":
    asyncio.run(main())
