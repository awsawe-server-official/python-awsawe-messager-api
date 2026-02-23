import requests

url = 'https://awsawe-server.ru/'

session = requests.Session()

def authorization(username, password):
    auth_url = f"{url}authorization"
    login_data = {
        "username": username,
        "password": password
    }
    
    response = session.post(auth_url, data=login_data)
    return response.json()

def send(config, text):
    username = config['username']
    password = config['password']
    chat_id = config['chat_id']
    debug = config.get('debug', 'false')
    
    auth_result = authorization(username, password)
    
    if auth_result.get('success'):
        url_send = f"{url}api/user/chat/{chat_id}/send"
        message_data = {"text": text}
        
        response = session.post(url_send, json=message_data)
        result = response.json()
        
        if debug == "true":
            if result.get('success'):
                print("✅ Сообщение успешно отправлено и зашифровано")
                print(f"ID сообщения: {result.get('message_id')}")
                print(f"Время отправки: {result.get('time_display')}")
            else:
                print(f"❌ Ошибка при отправке: {result.get('message')}")
        
        return result
    else:
        if debug == "true":
            print(f"❌ Ошибка авторизации: {auth_result.get('message')}")
        return auth_result

def recv(config):
    username = config['username']
    password = config['password']
    chat_id = config['chat_id']
    include_system = config.get('include_system', 'false')
    decrypt = config.get('decrypt', 'true')
    debug = config.get('debug', 'false')
    
    auth_result = authorization(username, password)
    
    if auth_result.get('success'):
        url_recv = f"{url}api/user/chat/{chat_id}/messages"
        
        params = {
            "limit": 1,
            "offset": 0,
            "decrypt": decrypt,
            "include_system": include_system
        }
        
        response = session.get(url_recv, params=params)
        data = response.json()
        
        if debug == "true":
            if data.get('success'):
                message = data['messages'][0]
                print(f"📨 [{message['time_display']}] {message.get('user', 'Система')}: {message['text']}")
            else:
                print(f"❌ Ошибка при получении сообщений: {data.get('message')}")
        
        return data
    else:
        if debug == "true":
            print(f"❌ Ошибка авторизации: {auth_result.get('message')}")
        return auth_result