# -- coding: utf-8 --

import requests
ApiKey = ""
data = requests.get(f"https://youtube.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&moderationStatus=published&videoId=lF3RKuiFpn8&key={ApiKey}")

print(data.content)
