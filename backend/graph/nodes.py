from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from typing import List
from graph.state import ImageGenState
from services.llm import get_llm
from services.flux import generate_flux_image


llm = get_llm()


# ---------- Structured Outputs ----------

class Plan(BaseModel):
    steps: List[str] = Field(description="Ordered steps for image generation")


class Critique(BaseModel):
    pass_quality: bool
    issues: List[str]
    suggestion: str


# ---------- Nodes ----------

async def plan_node(state: ImageGenState):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert creative planner."),
        ("user", "{input}")
    ])

    planner = prompt | llm.with_structured_output(Plan)
    plan = await planner.ainvoke({"input": state["user_input"]})

    return {
        "plan_steps": plan.steps,
        "state_log": [f"Planned steps: {plan.steps}"],
    }


async def refine_prompt_node(state: ImageGenState):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You refine ideas into Flux-optimized image prompts."),
        ("user", f"Idea: {state['user_input']}\nSteps: {state['plan_steps']}")
    ])

    refined = await llm.ainvoke(prompt.format_messages())
    refined_prompt = refined.content.strip()

    return {
        "refined_prompt": refined_prompt,
        "past_steps": [("Refined Prompt", refined_prompt)],
        "state_log": ["Refined prompt for Flux diffusion"],
    }


async def generate_image_node(state: ImageGenState):
    image_path = await generate_flux_image(state["refined_prompt"])

    return {
        "image_path": image_path,
        "state_log": [f"Generated image at: {image_path}"],
    }


async def critique_node(state: ImageGenState):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a strict image quality critic."),
        ("user", f"Prompt: {state['refined_prompt']}")
    ])

    critic = prompt | llm.with_structured_output(Critique)
    critique = await critic.ainvoke({})

    return {
        "critique": critique.dict(),
        "state_log": [f"Critique result: {critique.dict()}"],
    }


def decision_node(state: ImageGenState) -> str:
    if not state["critique"]["pass_quality"] and state["iteration"] < 1:
        return "refine"
    return "end"
