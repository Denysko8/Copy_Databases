import requests
import threading
import time

# Вставте сюди URL вашого Cloud Run сервісу
URL = "https://flask-app-598838815033.europe-central2.run.app/" 

# Параметри навантаження
NUM_THREADS = 20  # Кількість одночасних "користувачів"
DURATION = 60     # Тривалість тесту в секундах

def spam_requests():
    start_timer = time.time()
    while time.time() - start_timer < DURATION:
        try:
            # Відправляємо запит і чекаємо відповідь
            resp = requests.get(URL)
            # Можна розкоментувати для перевірки, чи йдуть запити успішно (код 200)
            # print(f"Response: {resp.status_code}") 
        except Exception as e:
            print(f"Error: {e}")

print(f"🚀 Починаємо навантаження на {URL}...")
threads = []
# Запускаємо потоки
for _ in range(NUM_THREADS):
    t = threading.Thread(target=spam_requests)
    t.start()
    threads.append(t)

# Чекаємо завершення всіх потоків
for t in threads:
    t.join()

print("✅ Тест завершено.")