"""Event publisher — sends events to Valkey pub/sub."""

import json
from dataclasses import asdict

# TODO(agent): Initialize Valkey client from settings.valkey_url
# valkey_client = None


async def publish_event(event: object) -> None:
    """Publish an event to the Valkey pub/sub channel."""
    # TODO(agent): Implement Valkey pub/sub publishing:
    #   channel = event.channel
    #   payload = json.dumps(asdict(event))
    #   await valkey_client.publish(channel, payload)
    pass
