"""TutorAgent graph nodes — retrieve_context, socratic_respond, offer_hint."""

from agents.tutor.state import TutorState


async def retrieve_context(state: TutorState) -> TutorState:
    """Retrieve relevant context from Weaviate for the student's question."""
    # TODO(agent): Call packages/rag/rag/retriever.py::retrieve
    return {**state, "retrieved_context": []}


async def socratic_respond(state: TutorState) -> TutorState:
    """Generate a Socratic response using RAG context."""
    # TODO(agent): Format prompt with context + history, call LLM (task_type="tutoring")
    return {**state, "response": "", "citations": []}


async def offer_hint(state: TutorState) -> TutorState:
    """Check if student should be offered a hint based on attempt count."""
    # TODO(agent): Check attempt_count threshold, set hint_offered flag
    return {**state, "hint_offered": False}
