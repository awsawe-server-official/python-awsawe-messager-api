from awsawe_messager_api import bot

config = {
    'bot_id': '123456789',
    'bot_token': 'ваш_токен',
    'chat_id': '987654321',
    'include_system': 'true',     # Включить системные сообщения
    'debug': 'true'
}

# Получение последних сообщений
while True:
    messages = bot.recv(config)
    print(messages)
