"""TutorAgent — LangGraph workflow for Socratic tutoring."""

from langgraph.graph import END, StateGraph

from agents.base import BaseAgent
from agents.tutor.nodes import offer_hint, retrieve_context, socratic_respond
from agents.tutor.state import TutorState


class TutorAgent(BaseAgent):
    def build_graph(self) -> StateGraph:
        graph = StateGraph(TutorState)

        graph.add_node("retrieve_context", retrieve_context)
        graph.add_node("socratic_respond", socratic_respond)
        graph.add_node("offer_hint", offer_hint)

        graph.set_entry_point("retrieve_context")
        graph.add_edge("retrieve_context", "socratic_respond")
        graph.add_edge("socratic_respond", "offer_hint")
        graph.add_edge("offer_hint", END)

        return graph.compile()
