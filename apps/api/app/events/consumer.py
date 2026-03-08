"""Event consumer — subscribes to Valkey channels and triggers agent workflows."""


async def start_event_consumer() -> None:
    """Start listening for events on Valkey pub/sub channels.

    Routes events to appropriate agent handlers:
    - ingestion.started → IngestionAgent
    - submission.received → GraderAgent → GameAgent
    - grade.awarded → AnalyticsAgent
    """
    # TODO(agent): Implement event consumer:
    #   1. Subscribe to all relevant channels
    #   2. Parse incoming messages
    #   3. Route to appropriate handler
    #   4. Handle errors gracefully (dead letter queue)
    pass
