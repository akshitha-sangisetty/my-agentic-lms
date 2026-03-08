"""
Feedback generation service — creates prescriptive learning recommendations.
"""


async def generate_feedback(grade_result: dict, knowledge_graph: dict) -> str:
    """Generate prescriptive feedback based on grading results.

    Identifies knowledge gaps and suggests targeted mini-quizzes.
    """
    # TODO(agent): Implement feedback generation:
    #   1. Analyze which rubric criteria scored low
    #   2. Map low-scoring criteria to Knowledge Graph concepts
    #   3. Generate specific remediation suggestions
    #   4. Optionally create bonus mini-quiz for weak concepts
    return ""
