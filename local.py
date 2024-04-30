import requests

res = requests.put("http://127.0.0.1:3000/api/Streams/2", {"name": "Valorant", "Streams": 5})
print(res.json())
