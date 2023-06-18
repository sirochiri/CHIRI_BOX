import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_addr.connect(("www.google.co.kr", 443))
    # www.google.co.kr 에 접속한다. https의 기본 접속 포트는 443.

print(in_addr.getsockname()[0])
    # 연결된 소켓의 이름을 출력