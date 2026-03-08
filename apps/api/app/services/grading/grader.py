"""
Grading service — orchestrates the GraderAgent for submission evaluation.
"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


async def grade_submission(submission_id: UUID, db: AsyncSession) -> dict:
    """Grade a submission using the GraderAgent.

    Steps:
    1. Load submission + assignment rubric + source material
    2. Call GraderAgent.evaluate(submission, rubric, sources)
    3. Run consistency check (3x re-grade, check variance)
    4. Update submission with ai_grade + feedback
    5. Trigger GameAgent for XP/Gold update
    """
    # TODO(agent): Implement grading pipeline.
    #   See packages/agents/agents/grader/ for the GraderAgent.
    return {}
