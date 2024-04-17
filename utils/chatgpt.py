from openai import OpenAI
from utils.tokens import openai_id
from db import Database

client = OpenAI(api_key=f"{openai_id}", base_url="https://api.proxyapi.ru/openai/v1")
db = Database("./database.db")


def get_chat_completion(user_id: int, user_message, conversation_history:list=None):

    # Если история диалога не предоставлена, инициализируем пустым списком
    if conversation_history is None:
        conversation_history = []

    # Добавляем сообщение пользователя в историю диалога
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
      model="gpt-3.5-turbo-0613",
      messages=conversation_history
    )
    db.add_used_tokens(user_id, response.usage.total_tokens)
    print(db.get_used_tokens(user_id))
    return response.choices[0].message.content
