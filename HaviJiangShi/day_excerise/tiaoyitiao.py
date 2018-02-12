import requests
import json
import time
from Crypto.Cipher import AES
import base64

session_id = "NOyKnA9YrN0PO50MvdYMB2qhocLTQqW7c79xkxKmYxvh8kOvgSr1FzuNkZF4Tvv/aUfFhajw2DvwswwHoDi+VKj6KqPn1wwkP10WAfFmrpj4/mcC6G5j+C+fQtZreGBi8I6KG/f97uce7mRN5vB7gg=="
times = 415
#获取当前时间
time_now = int(time.time())
#转换成localtime
time_local = time.localtime(time_now)
#转换成新的时间格式(2016-05-09 18:59:20)
dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)


#转换成时间数组
timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
#转换成时间戳
timestamp = int(time.mktime(timeArray))
print(timestamp)
battleReport = {
	"base_req": {
		"session_id": session_id,
		"fast": 1,
		"client_info": {
			"platform": "ios",
			"model": "iPhone 6<iPhone7,2>",
			"system": "iOS 11.2.1"
		}
	},
	"report_list": [{
		"ts": timestamp,
		"type": 10
	}, {
		"ts": timestamp + 1000,
		"type": 2,
		"score": 800,
		"best_score": 196,
		"break_record": 0,
		"duration": 9,
		"times": times
	}]
}

action_data = {
    "score": 800,
    "times": times,
    "game_data": "{}"
}

aes_key = session_id[0:16]
aes_iv  = aes_key

cryptor = AES.new(aes_key, AES.MODE_CBC, aes_iv)
print(aes_key)
str_action_data = json.dumps(action_data).encode("utf-8")
print("json_str_action_data ", str_action_data)

#Pkcs7
length = 16 - (len(str_action_data) % 16)
str_action_data += bytes([length])*length

cipher_action_data = base64.b64encode(cryptor.encrypt(str_action_data)).decode("utf-8")
print("action_data ", cipher_action_data)

post_data = {
  "base_req": {
    "session_id": session_id,
    "fast": 1,
  },
  "action_data": cipher_action_data
}

headers = {
    "charset": "utf-8",
    "Accept-Encoding": "gzip",
    "referer": "https://servicewechat.com/wx7c8d593b2c3a7703/3/page-frame.html",
    "content-type": "application/json",
    "User-Agent": "MicroMessenger/6.6.1.1200(0x26060130) NetType/WIFI Language/zh_CN",
    "Content-Length": "0",
    "Host": "mp.weixin.qq.com",
    "Connection": "Keep-Alive"
}

url = "https://mp.weixin.qq.com/wxagame/wxagame_settlement"
url1 = "https://mp.weixin.qq.com/wxagame/wxagame_bottlereport"

response1 = requests.post(url1, json=battleReport, headers=headers)
print(json.loads(response1.text))
response = requests.post(url, json=post_data, headers=headers)
print(json.loads(response.text))