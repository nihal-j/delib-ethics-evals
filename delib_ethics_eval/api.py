"""OpenAI-compatible API wrapper. Uses env vars: OPENAI_API_KEY, OPENAI_BASE_URL, MODEL."""

import os
from openai import OpenAI


def _client() -> OpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is required")
    base_url = os.environ.get("OPENAI_BASE_URL")
    return OpenAI(api_key=api_key, base_url=base_url if base_url else None)


def default_model() -> str:
    return os.environ.get("MODEL", "openai/gpt-3.5-turbo")


def completion(messages: list[dict], json_mode: bool = True, model: str | None = None) -> str:
    """Call the API and return the assistant content string."""
    client = _client()
    model = model or default_model()
    kwargs = {"model": model, "messages": messages}
    if json_mode:
        kwargs["response_format"] = {"type": "json_object"}
    resp = client.chat.completions.create(**kwargs)
    content = resp.choices[0].message.content
    if content is None:
        return ""
    return content.strip()
