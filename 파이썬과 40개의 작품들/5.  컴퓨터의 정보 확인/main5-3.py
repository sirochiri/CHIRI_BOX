import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    print(f'CPU사용량: {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3,1)
    print(f'사용 가능한 메모리: {memory_avail} GB')

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2
    
    sent = round(curr_sent-prev_sent,1)
    recv = round(curr_recv-prev_recv,1)

    print(f'보내기: {sent} MB  받기: {recv} MB')

    prev_sent = curr_sent
    prev_recv = curr_recv

    # 10. CPU의 사용량을 1초(interval=1) 동안의 평균값을 구합니다.
    # 11. CPU의 사용량을 출력합니다.
    # 13-15. 사용 가능한 메모리를 출력합니다.
    # 17-27. 네트워크에서 보내고 받은 크기를 출력합니다.
    # 21. 현재 측정한 값에서 이전에 측정한 값을 뺌 = 1초동안 보내는 데이터

    # ctrl + c를 눌러서 종료