"""OpenAI / Cloud LLM provider — connects to OpenAI or any OpenAI-compatible API (Groq, OpenRouter, Gemini, etc.)."""

import os
import logging
from openai import AsyncOpenAI

from llm.provider import LLMProvider, LLMResponse

logger = logging.getLogger(__name__)


class OpenAIProvider(LLMProvider):
    """Provider for cloud OpenAI or OpenAI-compatible API endpoints."""

    def __init__(
        self,
        api_key: str | None = None,
        base_url: str | None = None,
        default_model: str = "gpt-4o-mini",
    ):
        resolved_key = (
            api_key
            or os.getenv("OPENAI_API_KEY")
            or os.getenv("LLM_API_KEY")
            or ""
        )
        resolved_base_url = (
            base_url
            or os.getenv("OPENAI_BASE_URL")
            or os.getenv("LLM_BASE_URL")
            or None
        )
        self.default_model = os.getenv("OPENAI_MODEL") or default_model

        kwargs: dict[str, str] = {"api_key": resolved_key}
        if resolved_base_url:
            kwargs["base_url"] = resolved_base_url

        self.client = AsyncOpenAI(**kwargs)

    async def complete(
        self,
        messages: list[dict],
        model: str,
        temperature: float = 0.7,
        max_tokens: int = 2048,
    ) -> LLMResponse:
        # If the requested model is a local/legacy identifier (like qwen or llama), map to configured cloud model
        use_model = model
        local_prefixes = ("qwen", "llama", "deepseek", "localhost", "mistral-local")
        if not model or any(prefix in model.lower() for prefix in local_prefixes):
            use_model = self.default_model

        response = await self.client.chat.completions.create(
            model=use_model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        choice = response.choices[0]
        usage = response.usage
        return LLMResponse(
            content=choice.message.content or "",
            model=response.model,
            prompt_tokens=usage.prompt_tokens if usage else 0,
            completion_tokens=usage.completion_tokens if usage else 0,
            total_tokens=usage.total_tokens if usage else 0,
        )

    async def health_check(self) -> bool:
        try:
            await self.client.models.list()
            return True
        except Exception:
            return False
