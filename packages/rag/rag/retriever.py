"""Weaviate hybrid search retriever for RAG context."""

from dataclasses import dataclass


@dataclass
class RetrievedChunk:
    text: str
    source_doc: str
    source_page: int
    concept: str
    score: float


async def retrieve(
    query: str, collection_name: str, top_k: int = 5
) -> list[RetrievedChunk]:
    """Perform hybrid search (dense + sparse) on Weaviate.

    Returns top-k most relevant chunks with source attribution.
    """
    # TODO(agent): Implement Weaviate hybrid retrieval:
    #   1. Connect to Weaviate using weaviate-client v4
    #   2. Embed query using BGE-M3
    #   3. Perform hybrid search (alpha=0.7 for dense weighting)
    #   4. Return chunks with metadata
    return []
