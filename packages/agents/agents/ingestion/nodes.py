"""IngestionAgent graph nodes — parse, chunk, embed, build_graph."""

from agents.ingestion.state import IngestionState


async def parse(state: IngestionState) -> IngestionState:
    """Parse the uploaded file into structured page data."""
    # TODO(agent): Call the appropriate parser based on file_type:
    #   - PDF → services/ingestion/parser.py::parse_pdf
    #   - PPTX → parse_pptx
    #   - DOCX → parse_docx
    #   - MP4/MP3 → faster-whisper transcription
    return {**state, "current_step": "parsing", "progress_pct": 25, "parsed_pages": []}


async def chunk(state: IngestionState) -> IngestionState:
    """Split parsed content into semantic chunks."""
    # TODO(agent): Call services/ingestion/chunker.py::semantic_chunk
    return {**state, "current_step": "chunking", "progress_pct": 50, "chunks": []}


async def embed(state: IngestionState) -> IngestionState:
    """Embed chunks and store in Weaviate."""
    # TODO(agent): Call services/ingestion/embedder.py::embed_and_store
    return {**state, "current_step": "embedding", "progress_pct": 75, "embeddings_stored": 0}


async def build_graph(state: IngestionState) -> IngestionState:
    """Extract concepts and build Knowledge Graph in Neo4j."""
    # TODO(agent): Call packages/knowledge-graph/kg/builder.py
    return {
        **state,
        "current_step": "graph_building",
        "progress_pct": 100,
        "concept_nodes": [],
        "relationships": [],
    }
