import os
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.schema import SystemMessage, HumanMessage
from app.core.setting import settings
memory = ConversationBufferMemory(return_messages=True)

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.6,
    openai_api_key=settings.OPENAI_API_KEY,
)

def run_coach(prompt: str):
    """Run a contextual AI coaching session"""
    memory.chat_memory.add_user_message(prompt)
    messages = [
        SystemMessage(content="You are a focused productivity coach. Give concise, actionable advice."),
        *memory.chat_memory.messages,
    ]
    response = llm(messages)
    memory.chat_memory.add_ai_message(response.content)
    return response.content
