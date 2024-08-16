import requests

# resp = requests.post("http://127.0.0.1:5000", files={'file': open('test/three.png', 'rb')})
resp = requests.post("https://index-enq5l3mvca-as.a.run.app", files={'file': open('test/three.png', 'rb')})

# print(resp.status_code)
# print(resp.text)
print(resp.json())