# Sample Document

This is a sample document for testing the RAG application.

## Introduction

Retrieval Augmented Generation (RAG) is a technique that enhances large language models by incorporating external knowledge from a database or document collection.

## How RAG Works

1. **Document Ingestion**: Documents are processed, chunked, and embedded into vectors
2. **Storage**: Vector embeddings are stored in a vector database
3. **Retrieval**: When a query comes in, relevant document chunks are retrieved
4. **Generation**: The LLM generates a response using the retrieved context

## Benefits of RAG

- **Accurate Responses**: Answers are grounded in real documents
- **Reduced Hallucinations**: LLM has concrete context to work with
- **Up-to-date Information**: Knowledge base can be updated without retraining
- **Source Attribution**: Can cite specific documents used

## Use Cases

- Customer support chatbots
- Internal knowledge bases
- Document Q&A systems
- Research assistants
- Code documentation search

## Technical Stack

This RAG application uses:
- **LangChain**: Framework for building LLM applications
- **ChromaDB**: Vector database for embeddings
- **OpenAI**: For embeddings and text generation
- **FastAPI**: Web framework for the REST API

## Getting Started

1. Ingest your documents using the `/ingest` endpoint
2. Query your knowledge base using the `/query` endpoint
3. Get streaming responses with `/query/stream`

That's it! Your RAG application is ready to answer questions based on your documents.
