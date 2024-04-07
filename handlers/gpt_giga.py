from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router, F
from aiogram.filters.command import CommandObject
from dotenv import find_dotenv, load_dotenv
from os import getenv
import requests
import uuid
import json

router = Router()
router.message.filter(F.chat.type.in_({"private"}))
load_dotenv(find_dotenv())
auth = getenv('SBER_ID')

def get_token(auth_token, scope='GIGACHAT_API_PERS'):
    """
      Выполняет POST-запрос к эндпоинту, который выдает токен.

      Параметры:
      - auth_token (str): токен авторизации, необходимый для запроса.
      - область (str): область действия запроса API. По умолчанию — «GIGACHAT_API_PERS».

      Возвращает:
      - ответ API, где токен и срок его "годности".
      """

    rq_uid = str(uuid.uuid4())

    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json',
        'RqUID': rq_uid,
        'Authorization': f'Basic {auth_token}'
    }

    payload = {
        'scope': scope
    }

    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        return response
    except requests.RequestException as e:
        print(f"Ошибка: {str(e)}")
        return -1

def get_chat_completion(auth_token, user_message, conversation_history=None):
    """
    Отправляет POST-запрос к API чата для получения ответа от модели GigaChat в рамках диалога.

    Параметры:
    - auth_token (str): Токен для авторизации в API.
    - user_message (str): Сообщение от пользователя, для которого нужно получить ответ.
    - conversation_history (list): История диалога в виде списка сообщений (опционально).

    Возвращает:
    - response (requests.Response): Ответ от API.
    - conversation_history (list): Обновленная история диалога.
    """
    # URL API, к которому мы обращаемся
    url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

    # Если история диалога не предоставлена, инициализируем пустым списком
    if conversation_history is None:
        conversation_history = []

    # Добавляем сообщение пользователя в историю диалога
    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    # Подготовка данных запроса в формате JSON
    payload = json.dumps({
        "model": "GigaChat:latest",
        "messages": conversation_history,
        "temperature": 1,
        "top_p": 0.1,
        "n": 1,
        "stream": False,
        "max_tokens": 512,
        "repetition_penalty": 1,
        "update_interval": 0
    })

    # Заголовки запроса
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth_token}'
    }

    # Выполнение POST-запроса и возвращение ответа
    try:
        response = requests.post(url, headers=headers, data=payload, verify=False)
        response_data = response.json()

        # Добавляем ответ модели в историю диалога
        conversation_history.append({
            "role": "assistant",
            "content": response_data['choices'][0]['message']['content']
        })

        return response, conversation_history
    except requests.RequestException as e:
        # Обработка исключения в случае ошибки запроса
        print(f"Произошла ошибка: {str(e)}")
        return None, conversation_history


response = get_token(auth)
if response != 1:
  print(response.text)
  giga_token = response.json()['access_token']

url = "https://gigachat.devices.sberbank.ru/api/v1/models"

payload={}
headers = {
  'Accept': 'application/json',
  'Authorization': f'Bearer {giga_token}'
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

@router.message(Command("gpt_giga"))
async def cmd_gpt_giga(message: Message, command: CommandObject):
    if command.args is None:
        await message.answer("Ошибка: нет аргументов.")
        return
    query = command.args.split(" ", maxsplit=0)
    if 'conversation_history' not in globals():
        global conversation_history
        response, conversation_history = get_chat_completion(giga_token, query[0])
    else:
        response, conversation_history = get_chat_completion(giga_token, query[0], conversation_history)
    response = f"{response.json()['choices'][0]['message']['content']}\n----------------------------------------------------------------\nЗакончить диалог - \cancel"
    await message.reply(f"{response}", parse_mode="MarkDown")
