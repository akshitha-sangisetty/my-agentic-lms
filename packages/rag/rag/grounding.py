"""Hallucination detection — verifies AI claims against source context."""


async def check_grounding(response: str, context: str) -> dict:
    """Check if an AI response is grounded in the provided context.

    Returns: {"grounded": bool, "ungrounded_claims": [...], "confidence": float}
    """
    # TODO(agent): Implement grounding check:
    #   1. Extract claims from the AI response
    #   2. For each claim, search for supporting evidence in context
    #   3. Flag claims without evidence as "ungrounded"
    #   4. Block responses with >20% ungrounded claims
    return {"grounded": True, "ungrounded_claims": [], "confidence": 1.0}
