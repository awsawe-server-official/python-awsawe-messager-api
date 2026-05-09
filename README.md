# awsawe_messager_api

<div align="center">
  
### 🚀 Библиотека для работы с AI Messenger API
  
[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)]()

</div>

## 📋 Содержание

- [О библиотеке](#о-библиотеке)
- [Требования](#требования)
- [Установка](#установка)
- [Быстрый старт](#быстрый-старт)
- [BOT API](#bot-api)
- [USER API](#user-api)
- [Параметры конфигурации](#параметры-конфигурации)
- [Примеры ответов](#примеры-ответов)
- [Обработка ошибок](#обработка-ошибок)
- [Поддержка](#поддержка)

## 📖 О библиотеке

`awsawe_messager_api` — это удобная Python-библиотека для взаимодействия с AI Messenger API. Поддерживает два режима работы:

| Режим | Шифрование | Назначение |
|-------|------------|------------|
| **Bot API** | ❌ Нет | Создание простых ботов |
| **User API** | ✅ Да | Работа от имени пользователя |

## 🔧 Требования

| Компонент | Версия |
|-----------|--------|
| Python | 3.6 или выше |
| requests | Последняя стабильная |

## 📦 Установка

```bash
# Клонирование библиотеки
git clone https://github.com/awsawe-server-official/python-awsawe-messager-api.git
🚀 Быстрый старт
python
🤖 BOT API
Bot API не использует шифрование и идеально подходит для создания простых ботов.

📤 Отправка сообщения
python
from awsawe_messager_api import bot

config = {
    'bot_id': '123456789',      # ID вашего бота
    'bot_token': 'ваш_токен',    # Токен бота
    'chat_id': '987654321',      # ID чата
    'debug': 'true'               # Показывать отладочную информацию
}

# Отправка сообщения
result = bot.send(config, "Привет! Я бот!")
print(result)
📥 Получение сообщений
python
from awsawe_messager_api import bot

config = {
    'bot_id': '123456789',
    'bot_token': 'ваш_токен',
    'chat_id': '987654321',
    'include_system': 'true',     # Включить системные сообщения
    'debug': 'true'
}

# Получение последних сообщений
messages = bot.recv(config)
print(messages)
👤 USER API
User API использует шифрование сообщений и требует авторизации пользователя.

📤 Отправка сообщения
python
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
📥 Получение сообщений
python
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
messages = user.recv(config)
print(messages)
