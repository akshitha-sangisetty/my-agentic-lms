"""
Leaderboard service — Valkey sorted set backed class rankings.
"""

from uuid import UUID


async def update_leaderboard(course_id: UUID, student_id: UUID, xp_total: int) -> None:
    """Update student's XP on the course leaderboard."""
    # TODO(agent): Implement Valkey sorted set update:
    #   await valkey.zadd(f"leaderboard:{course_id}", {str(student_id): xp_total})
    pass


async def get_leaderboard(course_id: UUID, limit: int = 10) -> list[dict]:
    """Get top N students on the leaderboard."""
    # TODO(agent): Implement Valkey ZREVRANGE:
    #   results = await valkey.zrevrange(f"leaderboard:{course_id}", 0, limit-1, withscores=True)
    return []


async def get_rank(course_id: UUID, student_id: UUID) -> int | None:
    """Get student's rank on the leaderboard."""
    # TODO(agent): Implement Valkey ZREVRANK:
    #   rank = await valkey.zrevrank(f"leaderboard:{course_id}", str(student_id))
    return None
