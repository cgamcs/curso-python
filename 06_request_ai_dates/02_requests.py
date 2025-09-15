# 1. Sin dependencias
import json
import urllib.request

api_post = "https://jsonplaceholder.typecode.com/pets/"

try:
  response = urllib.request.urlopen(api_post)
  data = response.read()
  json_data = json.loads(data.decode('utf-8'))
  print(json_data)
  response.close()
except urllib.error.URLError as e:
  print(f"Error en la solicitud: {e}")

# 2. Con dependencia (requests)
import requests

try:
  print("\GET")
  response = requests.get(api_post)
  json = response.json()
  print(f"UserID: {json[0]['userId']}")
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

#--------
print("\nPOST:")
try:
  input = {
    "userId": 5,
    "title": "Cesar",
    "body": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit."
  }
  response = requests.post(api_post, json=input)
  print(response.json())
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

#--------
print("\nPUT:")
try:
  input = {
    "userId": 5,
    "id": 1,
    "title": "Cesar",
    "body": "Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit."
  }
  response = requests.put(f"{api_post}1", json=input)
  print(response.json())
except requests.exceptions.RequestException as e:
  print(f"Error en la solicitud: {e}")

# Usar la API de GPT-4o de OpenAI
OPENAI_KEY = ""
url = "https://api.openai.com/v1/chat/completions"