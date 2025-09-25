# Medical RAG ChatBot 🏥🤖

A smart medical chatbot that uses Retrieval-Augmented Generation (RAG) to provide medical information based on PDF documents. Built with FastAPI, LangChain, Pinecone, and OpenAI GPT-4.

## Features

- 📄 **PDF Document Processing**: Loads and processes medical PDF documents
- 🔍 **Semantic Search**: Uses HuggingFace embeddings for document similarity search
- 🧠 **AI-Powered Responses**: Leverages OpenAI GPT-4 for intelligent medical Q&A
- 💾 **Vector Database**: Pinecone integration for efficient document retrieval
- 🌐 **Web Interface**: Clean, responsive chat interface
- ⚡ **FastAPI Backend**: High-performance API with automatic documentation

## Tech Stack

- **Backend**: FastAPI, Python 3.8+
- **AI/ML**: LangChain, OpenAI GPT-4, HuggingFace Transformers
- **Vector DB**: Pinecone
- **Frontend**: HTML, CSS, JavaScript
- **Document Processing**: PyPDF

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Pinecone API key
- PDF medical documents (for training)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/MedBot.git
   cd MedBot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   PINECONE_API_KEY=your_pinecone_api_key_here
   ```

4. **Prepare your medical documents**
   - Place PDF files in a `data/` directory
   - Run the document processing script to populate Pinecone

## Usage

### Starting the Application

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

The application will be available at `http://localhost:8000`

### Web Interface

1. Navigate to `http://localhost:8000`
2. Type your medical questions in the chat interface
3. Get AI-powered responses based on your document knowledge base


## How It Works

1. **Document Processing**: PDFs are loaded and split into chunks using `RecursiveCharacterTextSplitter`
2. **Embeddings**: Text chunks are converted to vectors using HuggingFace's `all-MiniLM-L6-v2` model
3. **Vector Storage**: Embeddings are stored in Pinecone for fast similarity search
4. **Retrieval**: User questions trigger semantic search to find relevant document chunks
5. **Generation**: OpenAI GPT-4 generates responses based on retrieved context

## Configuration

### Embedding Model
The system uses `sentence-transformers/all-MiniLM-L6-v2` which produces 384-dimensional vectors. You can modify this in `src/helper.py`.

### Chunk Settings
- **Chunk Size**: 500 characters
- **Chunk Overlap**: 20 characters
- **Search Results**: Top 3 similar documents

### Model Settings
- **LLM**: OpenAI GPT-4o
- **Search Type**: Similarity search
- **Vector Database**: Pinecone

## API Documentation

Once the application is running, visit `http://localhost:8000/docs` for interactive API documentation.



## Disclaimer

This chatbot is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare providers for medical concerns.

