from fastapi import APIRouter
from pydantic import BaseModel
from graph.workflow import build_workflow

router = APIRouter()
workflow = build_workflow()


class GenerateRequest(BaseModel):
    idea: str
    style: str | None = None


@router.post("/generate")
async def generate(req: GenerateRequest):
    initial_state = {
        "user_input": req.idea,
        "structured_prompt": {},
        "refined_prompt": "",
        "image_path": "",
        "critique": {},
        "final_response": None,
        "iteration": 0,
        "error": None,
        "plan_steps": [],
        "past_steps": [],
        "state_log": [],
    }

    config = {
        "configurable": {"thread_id": "ppg-session"},
        "recursion_limit": 20,
    }

    final_state = None
    async for state in workflow.astream(initial_state, config, stream_mode="values"):
        final_state = state

    return {
        "image_url": final_state["image_path"],
        "final_prompt": final_state["refined_prompt"],
        "critique": final_state["critique"],
        "state_log": final_state["state_log"],
        "past_steps": final_state["past_steps"],
    }
