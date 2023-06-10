import json
import requests
import os
import time
from datetime import datetime
from datetime import timedelta

time_stamp = time.time()
utc_time = datetime.utcfromtimestamp(time_stamp)
time1 = (utc_time + timedelta(hours=+8))
today_date = time1.strftime("%Y/%m%d")
calendar_url = "https://img.owspace.com/Public/uploads/Download/" + today_date + ".jpg"

# 添加时间戳
time_stamp = time.time()
utc_time = datetime.utcfromtimestamp(time_stamp)
time1 = str(utc_time + timedelta(hours=+8))

# 定义要发送的消息
message = {
      "content": "This is today's one-way calendar"+"\n Time(UTC+8):"+time1,
      "embeds": [
        {
          "image": {
            "url": calendar_url
          }
        }
      ]
    }

# 定义请求头，包括机器人令牌和消息类型
bot_token = os.environ["bot_token"]
headers = {
    'Authorization': 'Bot ' + bot_token,
    'Content-Type': 'application/json'
}

# 定义请求 URL，包括要发送消息的频道 ID
discord_url = "https://discord.com/api/v10/channels/1091667161426182234/messages"
url = discord_url

# 发送 POST 请求，包括要发送的消息和请求头
response = requests.post(url, data=json.dumps(message), headers=headers)

# 打印响应
print(response.text)
