import asyncio
from knowledge.notion_knowledge_imp import NotionKnowledgeImp


async def main():
    print("Hello from data-integration-rag!")
    notion_knowledge = NotionKnowledgeImp()
    await notion_knowledge.initialize()

if __name__ == "__main__":
    asyncio.run(main())
