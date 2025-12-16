from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from app.graph.state import ImageGenState
from app.graph.nodes import (
    plan_node,
    refine_prompt_node,
    generate_image_node,
    critique_node,
    decision_node,
)


def build_workflow():
    graph = StateGraph(ImageGenState)

    graph.add_node("plan", plan_node)
    graph.add_node("refine", refine_prompt_node)
    graph.add_node("generate", generate_image_node)
    graph.add_node("critique", critique_node)

    graph.add_edge(START, "plan")
    graph.add_edge("plan", "refine")
    graph.add_edge("refine", "generate")
    graph.add_edge("generate", "critique")

    graph.add_conditional_edges(
        "critique",
        decision_node,
        {
            "refine": "refine",
            "end": END,
        },
    )

    return graph.compile(checkpointer=MemorySaver())
