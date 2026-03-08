"""TutorAgent state definition."""

from typing import TypedDict


class TutorState(TypedDict):
    student_id: str
    assignment_id: str
    question: str
    conversation_history: list[dict]
    retrieved_context: list[dict]
    response: str
    citations: list[dict]
    hint_offered: bool
    hint_tier: int
    hint_cost: int
    attempt_count: int
    errors: list[str]
