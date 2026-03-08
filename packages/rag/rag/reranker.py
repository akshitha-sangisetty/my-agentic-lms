"""Cross-encoder reranking for improved retrieval quality."""

from dataclasses import dataclass


async def rerank(query: str, chunks: list[dict], top_k: int = 3) -> list[dict]:
    """Rerank retrieved chunks using a cross-encoder model.

    Takes initial retrieval results and reorders them by relevance.
    """
    # TODO(agent): Implement cross-encoder reranking:
    #   1. Load cross-encoder model (e.g., ms-marco-MiniLM)
    #   2. Score each (query, chunk) pair
    #   3. Sort by score descending
    #   4. Return top_k
    return chunks[:top_k]
