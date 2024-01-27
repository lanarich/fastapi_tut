import httpx
import json

# Замените URL на фактический адрес вашего FastAPI-сервиса
base_url = "http://127.0.0.1:8000"

# GET-запрос
#response_get = httpx.get(f"{base_url}/dog")
#print(response_get.json())
#print(json.dumps(response_get.json(), indent=1))




new_dog_data = ('{\n'
                '    "name": "VOVA",\n'
                '    "pk": 0,\n'
                '    "kind": "terrier"\n'
                '}\n')

response_post = httpx.post(f"{base_url}/dog", json=json.loads(new_dog_data))
print("POST Response:", response_post.json())
