import httpx
from app.core.settings import settings

async def ask_openai(prompt: str, model: str = "gpt-3.5-turbo"):
    """Send a direct request to the OpenAI model without LangChain"""
    if not settings.OPENAI_API_KEY:
        return {"error": "Missing OpenAI API key"}

    headers = {"Authorization": f"Bearer {settings.OPENAI_API_KEY}"}
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=30,
        )

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    return {
        "answer": data["choices"][0]["message"]["content"],
        "tokens": data.get("usage", {}),
    }
