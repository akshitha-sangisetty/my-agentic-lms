"""
Content parsing service — extracts text from uploaded files.

Supports: PDF (via PyMuPDF), PPTX, DOCX.
Audio/video transcription handled separately via faster-whisper.
"""

from pathlib import Path


async def parse_pdf(file_path: Path) -> list[dict]:
    """Extract text and images from a PDF file.

    Returns a list of page dicts: [{"page": 1, "text": "...", "images": [...]}]
    """
    # TODO(agent): Implement PDF parsing with PyMuPDF (fitz):
    #   1. Open PDF with fitz.open(file_path)
    #   2. Iterate pages, extract text with page.get_text()
    #   3. For scanned pages (empty text), run OCR
    #   4. Extract images with page.get_images()
    #   5. Return structured page data
    return []


async def parse_pptx(file_path: Path) -> list[dict]:
    """Extract text from PPTX slides."""
    # TODO(agent): Implement PPTX parsing with python-pptx:
    #   1. Open presentation
    #   2. Iterate slides → shapes → text_frames
    #   3. Extract speaker notes
    #   4. Extract embedded images
    return []


async def parse_docx(file_path: Path) -> list[dict]:
    """Extract text from DOCX documents."""
    # TODO(agent): Implement DOCX parsing with python-docx:
    #   1. Open document
    #   2. Extract paragraphs, tables, headers
    #   3. Extract embedded images
    return []
