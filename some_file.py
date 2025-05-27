import requests
import time

API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7509133933:AAF0qn3sYQ2K5MSdQ7d4H_MW0PCme-AVDhY'
TEXT = 'Ура, классный апдейт!'
MAX_COUNTER = 100

offset = -2
counter = 0
chat_id : int

while counter < MAX_COUNTER:
    
    print(f'attempt = {counter}')

    updates = requests.get(f'{API_URL}{BOT_TOKEN}')