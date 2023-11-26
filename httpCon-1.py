import http.client
import urllib.parse
def subString(string,start,end):
    index = string.find(start.encode())
    next_string = ""
    if index != -1:
        # 如果找到了 NextURL，就从该位置开始截取字符串
        next_string = string[index + len(start):]
        # 再找到下一个 & 字符的位置，表示参数结束
        param_end = next_string.find(end.encode())
        if param_end != -1:
            next_string = next_string[:param_end]
    return next_string

if __name__ == '__main__':
    username = ""
    password = ""
    nasId = "52"
    url = "172.30.21.100"
    requestUrl = "1.1.1.1"
    conn1 = http.client.HTTPConnection(requestUrl)
    conn1.request("GET", "http://1.1.1.1/")
    r = conn1.getresponse()
    print(r.status, r.reason)
    data1 = r.read()
    print(data1)
    # 找到 NextURL 的位置
    next_data = subString(data1,"<NextURL>","</NextURL>")
    if(len(next_data)>1):
        ip = subString(next_data,"http://","/api/r/")
        print(ip)
        url = bytes(ip).decode()
        id = subString(next_data,"/api/r/","?userip=")
        print(id)
        nasId = id
    conn1.close()
    # 与服务器建立链接
    conn = http.client.HTTPConnection(url)
    #向服务器发送请求
    method="POST"
    requrl = "http://"+url+"/api/account/login"
    headerdata = {
        "Host": url,
        "Accept-Encoding": "gzip",
        "User-Agent": "Android-ALI-Moblie 1.3.0",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Connection": "Keep-Alive"
        }
    test_data = urllib.parse.urlencode({
        "username": username,
         "password": password,
         "nasId": nasId,
        })
    conn.request(method=method,url=requrl,body=test_data,headers = headerdata)

    # 获取响应消息体
    response = conn.getresponse()
    print(response.status, response.reason)
    data = response.read()
    print(data.decode("utf-8"))

    # 获取响应头部信息，列表形式
    resheader = response.getheaders();
    print(resheader)

    # 取出响应头部的Set-Cookie的值
    responsehead = response.getheader('Set-Cookie')
    print(responsehead)

    conn.close()