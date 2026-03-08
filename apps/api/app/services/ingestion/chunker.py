"""
Semantic chunking service — splits parsed content into concept-level chunks.

Uses LLM-assisted chunking: the model identifies concept boundaries rather than
splitting on arbitrary page/character limits.
"""


async def semantic_chunk(pages: list[dict], course_id: str) -> list[dict]:
    """Split parsed pages into semantic chunks grouped by concept.

    Returns: [{"chunk_id": "...", "text": "...", "concept": "...",
               "source_page": 1, "source_doc": "lecture1.pdf"}]
    """
    # TODO(agent): Implement semantic chunking:
    #   1. Concatenate page texts
    #   2. Use LLM (fast model) to identify concept boundaries
    #   3. Split at concept boundaries (not fixed-size)
    #   4. Tag each chunk with its primary concept
    #   5. Maintain source attribution (page, document)
    #   Target: chunks of 200-500 tokens, each covering one concept
    return []
