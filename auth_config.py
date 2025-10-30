import os
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    # Зчитуємо правильні дані з .env
    env_user = os.environ.get('API_USER')
    env_pass = os.environ.get('API_PASSWORD')
    
    # Перевіряємо, чи збігаються дані
    if username == env_user and password == env_pass:
        return username  # Успіх!
    return None  # Помилка автентифікації
