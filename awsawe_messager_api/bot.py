import requests

url = 'https://awsawe-server.ru/'

def send(config, text):
    bot_id = config['bot_id']
    bot_token = config['bot_token']
    chat_id = config['chat_id']
    debug = config.get('debug', 'false')

    headers = {
        "Authorization": f"Bot {bot_token}",
        "Content-Type": "application/json"
    }
    data = {
        "chat_id": chat_id,
        "text": text
    }
    
    response = requests.post(rf"{url}api/bot/{bot_id}/send", json=data, headers=headers)
    result = response.json()
    
    if debug == "true":
        if result.get('success'):
            print("✅ Сообщение успешно отправлено")
            print(f"ID сообщения: {result.get('message_id')}")
        else:
            print(f"❌ Ошибка: {result.get('message')}")
    
    return result

def recv(config):
    bot_id = config['bot_id']
    bot_token = config['bot_token']
    chat_id = config['chat_id']
    include_system = config.get('include_system', 'false')
    debug = config.get('debug', 'false')
    
    params = {
        "chat_id": chat_id, 
        "limit": 1,
        "include_system": include_system
    }
    headers = {"Authorization": f"Bot {bot_token}"}
    
    response = requests.get(rf"{url}api/bot/{bot_id}/messages", headers=headers, params=params)
    data = response.json()
    
    if debug == "true":
        if data.get('success'):
            message = data['messages']
            return message
        else:
            print(f"❌ Ошибка: {data.get('message')}")
    
    return data

def get_info(config):
    bot_id = config['bot_id']
    bot_token = config['bot_token']
    debug = config.get('debug', 'false')
    
    url_info = f"{url}api/bot/{bot_id}/info"
    headers = {"Authorization": f"Bot {bot_token}"}
    
    response = requests.get(url_info, headers=headers)
    data = response.json()
    
    if debug == "true":
        if data.get('success'):
            print(f"🤖 Информация о боте:")
            print(f"ID: {data.get('bot_id')}")
            print(f"Имя: {data.get('name')}")
        else:
            print(f"❌ Ошибка: {data.get('message')}")
    
    return data