"""
Tests for RAG application
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_health():
    """Test health check"""
    response = client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()


@pytest.mark.asyncio
async def test_query_no_documents():
    """Test query without ingested documents"""
    response = client.post(
        "/query",
        json={"query": "What is RAG?"}
    )
    assert response.status_code == 200
    result = response.json()
    assert "answer" in result
    assert "sources" in result


# Add more tests as needed
