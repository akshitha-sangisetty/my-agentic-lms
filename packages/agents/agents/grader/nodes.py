"""GraderAgent graph nodes — evaluate_criteria, generate_feedback, check_consistency."""

from agents.grader.state import GraderState


async def evaluate_criteria(state: GraderState) -> GraderState:
    """Evaluate submission against each rubric criterion."""
    # TODO(agent): Call LLM (task_type="grading") with rubric + submission + sources
    return {**state, "current_step": "evaluate_criteria", "grade_result": {}}


async def check_consistency(state: GraderState) -> GraderState:
    """Run consistency check — grade 3x and check variance."""
    # TODO(agent): Re-grade 2 more times, compare scores
    #   If variance > threshold, flag for human review
    return {
        **state,
        "current_step": "check_consistency",
        "consistency_check": {"scores": [], "variance": 0.0, "passed": True},
    }


async def generate_feedback(state: GraderState) -> GraderState:
    """Generate prescriptive feedback based on grading results."""
    # TODO(agent): Call LLM to generate actionable feedback
    return {**state, "current_step": "generate_feedback", "feedback": ""}
