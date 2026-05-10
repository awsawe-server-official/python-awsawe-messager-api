from awsawe_messager_api import user

config = {
    'username': 'ваш_логин',
    'password': 'ваш_пароль',
    'chat_id': '987654321',
    'include_system': 'true',      # Включить системные сообщения
    'decrypt': 'true',              # Расшифровывать сообщения
    'debug': 'true'
}

# Получение и расшифровка сообщений
while True:
    messages = user.recv(config)
    print(messages)
