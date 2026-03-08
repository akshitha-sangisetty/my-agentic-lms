"""
Streak tracking service — manages daily learning streaks.
"""

from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession


async def update_streak(student_id: UUID, db: AsyncSession) -> dict:
    """Update the student's streak based on activity today.

    Returns {"current_streak": int, "longest_streak": int, "streak_extended": bool}
    """
    # TODO(agent): Implement streak tracking:
    #   1. Check last activity timestamp for student
    #   2. If today: no change (already counted)
    #   3. If yesterday: increment streak
    #   4. If >1 day ago: check for streak freeze, reset if none
    #   5. Update longest_streak if current > longest
    return {"current_streak": 0, "longest_streak": 0, "streak_extended": False}
