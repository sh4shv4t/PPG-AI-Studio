import operator
from typing import Optional, List, Tuple, Dict
from typing_extensions import TypedDict, Annotated


class ImageGenState(TypedDict):
    # Core inputs / outputs
    user_input: str
    structured_prompt: Dict
    refined_prompt: str
    image_path: str
    critique: Dict
    final_response: Optional[str]

    # Control
    iteration: int
    error: Optional[str]

    # Explicit tracking
    plan_steps: List[str]
    past_steps: Annotated[List[Tuple[str, str]], operator.add]
    state_log: Annotated[List[str], operator.add]
