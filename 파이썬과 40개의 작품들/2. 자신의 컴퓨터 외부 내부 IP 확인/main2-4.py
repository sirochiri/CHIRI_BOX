import socket
import requests
import re

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
print("내부 IP: ", in_addr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]    #r >> raw string literals
print("외부 IP: ", out_addr)


# r로 시작하는 string을 "raw string literals"라고 하고, 이 경우 \가 특수문자가 아닌 그냥 \로 인식된다고 함.