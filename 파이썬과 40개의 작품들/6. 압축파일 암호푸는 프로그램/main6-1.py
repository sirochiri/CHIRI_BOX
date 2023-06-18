import itertools

passwd_string = "0123456789abscdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1, 4):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)

# 3. 숫자, 영문 소문자, 영문 대문자의 문자열을 바인딩
# 6. passw_string 모든 문자열을 repeat=길이의 조합을 반환합니다.
#    list안에 list가 있는 형태로 반환되는 듯 하다.
# 
# 7. 정렬하여 반환된 문자의 수만큼 반복합니다.
# 8. 리스트로 반환된 값을 문자열로 변환합니다.
#    ''.join(리스트)는 리스트의 값을 문자열로 변환합니다.
