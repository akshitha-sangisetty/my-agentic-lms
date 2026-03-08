"""DesignerAgent state definition."""

from typing import TypedDict


class DesignerState(TypedDict):
    course_id: str
    knowledge_graph: dict
    config: dict  # gamification_level, grading_strictness, types, count
    generated_assignments: list[dict]
    generated_rubrics: list[dict]
    current_step: str
    errors: list[str]
