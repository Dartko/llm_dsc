"""
curl http://localhost:11434/api/generate -d '{
  "model": "tinyllama",
  "prompt": "Why is the sky blue?",
  "stream": false
}'
"""

import requests
import json

url = 'http://localhost:11434/api/generate'

while True:
prompt= input("Promp: ")
data = {
    "model": "tinyllama",
    "prompt": prompt,
    "stream": False
  }

  headers = {
    "Content-Type: application/json"
  }

response = requests.post(url, json = data,headers= headers)

response = json.loads(response.text)

print(response["response"])
