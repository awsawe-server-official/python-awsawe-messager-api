"""
awsawe_messager_api - Библиотека для работы с AI Messenger API
Полная документация: https://awsawe-server.ru/api-docs

Поддерживает:
- User API (с шифрованием сообщений)
- Bot API (без шифрования)
"""

from . import user
from . import bot

__version__ = "1.0.0"
__author__ = "awsawe_1234"
__license__ = "Proprietary License"
__all__ = ['user', 'bot']