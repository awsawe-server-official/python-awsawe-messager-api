from awsawe_messager_api import user

config = {
    'username': 'ваш_логин',      # Имя пользователя
    'password': 'ваш_пароль',      # Пароль
    'chat_id': '987654321',        # ID чата
    'debug': 'true'                 # Показывать отладочную информацию
}

# Отправка зашифрованного сообщения
result = user.send(config, "Секретное сообщение!")
print(result)
