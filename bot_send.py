from awsawe_messager_api import bot

config = {
    'bot_id': '123456789',      # ID бота
    'bot_token': 'ваш_токен',    # Токен бота
    'chat_id': '987654321',      # ID чата
    'debug': 'true'               # Показывать отладочную информацию
}

# Отправка сообщения
result = bot.send(config, "Привет! Я бот!")
print(result)
