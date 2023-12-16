import requests

username = ""
password = ""
nasId = ""
url = f"http://172.30.21.100/api/account/login?username={username}&password={password}&nasId={nasId}"

payload = {}
headers = {
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
            'Cache-Control': 'no-cache',
            'connection': 'Keep-Alive',
            'Host': '172.30.21.100',
            'Pragma': 'no-cache',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'X-Requested-With': 'XMLHttpRequest'
        }

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
