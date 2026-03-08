"""
At-risk student detection — flags students based on engagement patterns.
"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


async def detect_at_risk_students(course_id: UUID, db: AsyncSession) -> list[dict]:
    """Identify students at risk of falling behind.

    Risk factors:
    - Low login frequency (< 2x/week)
    - Assignment completion rate < 50%
    - High hint dependency (> 3 hints per assignment avg)
    - Declining score trend
    - Streak breaks > 3 in last 2 weeks
    """
    # TODO(agent): Implement risk detection algorithm:
    #   1. Query submission + login data for enrolled students
    #   2. Score each risk factor (0.0-1.0)
    #   3. Compute weighted risk score
    #   4. Flag students above threshold
    #   5. Generate human-readable reason list
    return []
