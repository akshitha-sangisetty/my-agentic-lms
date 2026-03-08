"""DesignerAgent — LangGraph workflow for assignment generation."""

from langgraph.graph import END, StateGraph

from agents.base import BaseAgent
from agents.designer.nodes import generate_mcq, generate_rubrics, generate_scenarios, tag_concepts
from agents.designer.state import DesignerState


class DesignerAgent(BaseAgent):
    def build_graph(self) -> StateGraph:
        graph = StateGraph(DesignerState)

        graph.add_node("generate_mcq", generate_mcq)
        graph.add_node("generate_scenarios", generate_scenarios)
        graph.add_node("generate_rubrics", generate_rubrics)
        graph.add_node("tag_concepts", tag_concepts)

        graph.set_entry_point("generate_mcq")
        graph.add_edge("generate_mcq", "generate_scenarios")
        graph.add_edge("generate_scenarios", "generate_rubrics")
        graph.add_edge("generate_rubrics", "tag_concepts")
        graph.add_edge("tag_concepts", END)

        return graph.compile()
