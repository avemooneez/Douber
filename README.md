# Douber
### Документация

/start - команда для перезапуска бота, также при несуществовании юзера в БД команда служит регистратором

/help - команда для вывода текста с командами

/about - вывод информации о боте

/crypto - команда для вывода последней цены покупки выбранных криптовалют. Выбрать криптовалюты - /settings -> Crypto

/gpt - начать диалог с языковой моделью

/cancel - выход из диалога

/settings - команда для настройки некоторых других команд. 
/settings -> Crypto - настроить отображение криптовалют по команде /crypto.


### Как настроить бота?
1. Зайди в Телеграм, создай у @BotFather нового бота, скопируй токен. Вставь в файл .env.example в строку BOT_TOKEN вместо XXX
2. Зайди на страницу https://platform.openai.com/account, создай и скопируй ключ API в API Keys. Вставь в файл .env.example в строку OPENAI_ID вместо XXX
3. Создай виртуальное окружение командой ```python -m venv venv``` для Windows и ```python3 -m venv venv``` для Linux
4. Активируй командой ```venv\Scripts\activate.bat``` для Windows и ```source venv/bin/activate``` для Linux
5. Установи необходимые библиотеки и зависимости ```pip install -r requirements.txt```
6. Установи и настрой Redis. К сожалению, на это у автора нет инструкций
7. Самое время запускать! ```python3 main.py```

**Если что-то не сработает, а такое вполне может быть - пишите в Telegram: @mnz_pr**