"""DesignerAgent graph nodes — generate_mcq, generate_scenarios, generate_rubrics, tag_concepts."""

from agents.designer.prompts import PROMPTS
from agents.designer.state import DesignerState


async def generate_mcq(state: DesignerState) -> DesignerState:
    """Generate MCQ assignments from the Knowledge Graph."""
    # TODO(agent): Implement MCQ generation:
    #   1. Format prompt with concepts from knowledge_graph
    #   2. Call LLM router (task_type="creative")
    #   3. Parse and validate JSON response
    #   4. Create Assignment objects with type=MCQ
    return {**state, "current_step": "generate_mcq"}


async def generate_scenarios(state: DesignerState) -> DesignerState:
    """Generate branching scenario assignments."""
    # TODO(agent): Implement scenario generation
    return {**state, "current_step": "generate_scenarios"}


async def generate_rubrics(state: DesignerState) -> DesignerState:
    """Generate grading rubrics for all generated assignments."""
    # TODO(agent): Implement rubric generation for each assignment
    return {**state, "current_step": "generate_rubrics"}


async def tag_concepts(state: DesignerState) -> DesignerState:
    """Tag each assignment with the Knowledge Graph concepts it tests."""
    # TODO(agent): Implement concept tagging
    return {**state, "current_step": "tag_concepts"}
