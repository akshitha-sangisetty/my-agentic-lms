"""Base agent class with common patterns for all LangGraph agents."""

from abc import ABC, abstractmethod
from typing import Any


class BaseAgent(ABC):
    """Base class for all Agentic LMS agents.

    All agents follow the same lifecycle:
    1. Build the LangGraph StateGraph
    2. Compile it
    3. Run it with input state
    """

    @abstractmethod
    def build_graph(self) -> Any:
        """Build and return the compiled LangGraph."""
        ...

    async def run(self, input_state: dict) -> dict:
        """Execute the agent graph with the given input state."""
        graph = self.build_graph()
        result = await graph.ainvoke(input_state)
        return result
