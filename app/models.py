"""
Pydantic models for API requests and responses
"""
from pydantic import BaseModel, Field
from typing import List, Optional


class QueryRequest(BaseModel):
    """Query request schema"""
    query: str = Field(..., description="User query", min_length=1)
    top_k: Optional[int] = Field(None, description="Number of chunks to retrieve")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "What are the main topics in the documents?",
                "top_k": 4
            }
        }


class QueryResponse(BaseModel):
    """Query response schema"""
    query: str
    answer: str
    sources: List[str] = Field(default_factory=list)
    context_chunks: int = Field(0, description="Number of context chunks used")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "What are the main topics?",
                "answer": "The main topics include...",
                "sources": ["document1.pdf", "document2.pdf"],
                "context_chunks": 4
            }
        }


class IngestResponse(BaseModel):
    """Document ingestion response"""
    filename: str
    chunks_created: int
    status: str
    message: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "filename": "document.pdf",
                "chunks_created": 25,
                "status": "success",
                "message": "Document ingested successfully"
            }
        }
