# 🤖 Data Integration RAG System

[![Python](https://img.shields.io/badge/python-v3.12+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![RAG](https://img.shields.io/badge/tech-RAG-orange.svg)](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)

A sophisticated **Retrieval-Augmented Generation (RAG)** system that demonstrates advanced data integration capabilities across multiple sources. This project showcases modern AI/ML engineering practices for building scalable knowledge systems.

## 🎯 Project Overview

This system implements a multi-source RAG architecture that intelligently processes and indexes data from diverse platforms, enabling semantic search and knowledge retrieval across heterogeneous data sources.

### 🏗️ Architecture Highlights

- **Multi-Source Integration**: Seamlessly connects to Notion databases and MariaDB
- **Vector Database**: ChromaDB for efficient similarity search and document retrieval
- **Advanced Embeddings**: Google Gemini embeddings for state-of-the-art semantic understanding
- **Async Processing**: Full asynchronous architecture for optimal performance
- **Modular Design**: Clean separation of concerns with abstract base classes
- **Enterprise-Ready**: Robust error handling, logging, and configuration management

## 🚀 Key Features

### 📊 Data Sources
- **Notion Integration**: Automated extraction from Notion databases with metadata preservation
- **MariaDB Support**: Direct database connectivity with SQL query processing
- **Extensible Framework**: Abstract knowledge service interface for easy addition of new sources

### 🧠 AI/ML Components
- **Semantic Embeddings**: Powered by Google's Gemini AI for superior text understanding
- **Vector Storage**: ChromaDB for efficient similarity search and retrieval
- **Document Processing**: Intelligent metadata handling and content structuring
- **Real-time Indexing**: Automatic document processing and vector generation

### 🔧 Technical Stack

```python
# Core Technologies
- Python 3.12+
- ChromaDB (Vector Database)
- Google Gemini (Embeddings)
- SQLAlchemy (Database ORM)
- LangChain (Document Processing)
- Agno Framework (Knowledge Base Management)
```

## 📁 Project Structure

```
data-integration-rag/
├── main.py                          # Application entry point
├── knowledge/
│   ├── knowledge_service.py         # Abstract base class
│   ├── mariadb/
│   │   └── mariadb_knowledge_imp.py # MariaDB integration
│   └── notion/
│       └── notion_knowledge_imp.py  # Notion integration
├── handlers/
│   ├── database_data_handler.py     # Database metadata processing
│   └── metadata_handler.py          # Document metadata handling
├── utils/
│   └── logger/
│       └── logger.py               # Centralized logging
└── requirements.txt                # Dependencies
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.12+
- MariaDB Server (optional)
- Notion API Token (optional)
- Google AI API Key

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/devherik/data-integration-rag.git
   cd data-integration-rag
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Configure your credentials
   NOTION_TOKEN=your_notion_integration_token
   NOTION_ID=your_notion_database_id
   MARIADB_HOST=localhost
   MARIADB_PORT=3306
   MARIADB_USER=your_username
   MARIADB_PASSWORD=your_password
   GOOGLE_API_KEY=your_gemini_api_key
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 💡 Use Cases

### Enterprise Knowledge Management
- **Documentation Search**: Semantic search across technical documentation
- **Data Discovery**: Intelligent exploration of database schemas and content
- **Cross-Platform Integration**: Unified access to dispersed organizational knowledge

### AI-Powered Analytics
- **Semantic Querying**: Natural language queries across structured and unstructured data
- **Content Recommendations**: AI-driven content suggestions based on context
- **Knowledge Graphs**: Relationship discovery between different data sources

## 🎯 Key Achievements

- ✅ **Multi-Source RAG Implementation**: Successfully integrated multiple data sources into a unified retrieval system
- ✅ **Async Architecture**: Implemented fully asynchronous processing for optimal performance
- ✅ **Modular Design**: Created extensible framework allowing easy addition of new data sources
- ✅ **Production-Ready Code**: Includes comprehensive error handling, logging, and configuration management
- ✅ **AI Integration**: Leveraged cutting-edge embedding models for semantic understanding

## 🔮 Future Enhancements

- [ ] **Additional Data Sources**: Slack, Discord, GitHub, etc.
- [ ] **Query Interface**: RESTful API for external system integration
- [ ] **Real-time Sync**: Live updates from connected data sources
- [ ] **Advanced Analytics**: Usage metrics and performance monitoring
- [ ] **Multi-modal Support**: Image and document processing capabilities

## 🤝 Professional Context

This project demonstrates proficiency in:

- **AI/ML Engineering**: Practical implementation of RAG systems
- **Data Integration**: Multi-source data pipeline development
- **Software Architecture**: Clean, maintainable, and scalable code design
- **Async Programming**: High-performance concurrent processing
- **DevOps Practices**: Environment management and deployment readiness

---

### 📫 Connect with me on [LinkedIn](https://linkedin.com/in/herik-colares) to discuss AI/ML projects and data engineering solutions!

*This project showcases the intersection of modern AI capabilities with traditional data integration challenges, demonstrating how RAG systems can bridge the gap between diverse data sources and intelligent information retrieval.*