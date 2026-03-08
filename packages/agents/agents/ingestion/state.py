"""IngestionAgent state definition."""

from typing import TypedDict


class IngestionState(TypedDict):
    course_id: str
    file_path: str
    file_type: str  # pdf, pptx, docx, mp4, mp3
    parsed_pages: list[dict]
    chunks: list[dict]
    embeddings_stored: int
    concept_nodes: list[dict]
    relationships: list[dict]
    current_step: str
    progress_pct: int
    errors: list[str]
