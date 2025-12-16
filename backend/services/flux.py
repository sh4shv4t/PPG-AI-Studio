import os
import uuid
import requests

GENERATED_DIR = "generated"
os.makedirs(GENERATED_DIR, exist_ok=True)


def generate_flux_image(
    prompt: str,
    steps: int = 4,
    cfg_scale: float = 3.5,
    seed: int | None = None,
) -> str:
    """
    Lightweight Flux wrapper using Replicate-style HTTP.
    This keeps it free-tier deployable.

    NOTE:
    - On local dev without API key, returns a placeholder image.
    """

    api_key = os.getenv("REPLICATE_API_TOKEN")
    output_path = f"{GENERATED_DIR}/{uuid.uuid4().hex}.png"

    if not api_key:
        # Fallback for local dev / interviews
        with open(output_path, "wb") as f:
            f.write(b"")  # empty placeholder
        return output_path

    response = requests.post(
        "https://api.replicate.com/v1/predictions",
        headers={
            "Authorization": f"Token {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "version": "black-forest-labs/flux-schnell",
            "input": {
                "prompt": prompt,
                "num_inference_steps": steps,
                "guidance_scale": cfg_scale,
                "seed": seed,
            },
        },
        timeout=60,
    )

    response.raise_for_status()
    image_url = response.json()["output"][0]

    img_data = requests.get(image_url).content
    with open(output_path, "wb") as f:
        f.write(img_data)

    return output_path
