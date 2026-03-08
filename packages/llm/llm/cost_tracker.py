"""Token usage tracking per course for capacity planning."""

from dataclasses import dataclass, field


@dataclass
class UsageRecord:
    task_type: str
    model: str
    prompt_tokens: int
    completion_tokens: int
    course_id: str | None = None


class CostTracker:
    """Track LLM token usage for capacity planning and cost monitoring."""

    def __init__(self) -> None:
        self._records: list[UsageRecord] = []

    def record(self, usage: UsageRecord) -> None:
        self._records.append(usage)

    def get_total_tokens(self, course_id: str | None = None) -> int:
        records = self._records
        if course_id:
            records = [r for r in records if r.course_id == course_id]
        return sum(r.prompt_tokens + r.completion_tokens for r in records)

    # TODO(agent): Implement persistent storage of usage records.
    #   Store in PostgreSQL for historical analysis.
    #   Add Prometheus metrics for real-time monitoring.
