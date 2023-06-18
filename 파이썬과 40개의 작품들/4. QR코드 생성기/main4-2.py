import qrcode

file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, 'rt', encoding = 'UTF8') as f:
    read_lines = f.readlines()

    for line in read_lines:
        line = line.strip()
        print(line)

# 4. [4.  QR코드 생성기] 폴더에 [qr코드모음.txt] 파일을 읽습니다.
# 5. f.readlines()로 파일을 읽어 줄 별로 리스트의 값의 형태로 내어줍니다.
#    read_lines에는 줄별로 읽힌 값이 리스트 형태로 바인딩 됩니다.
#
# 7. 여러 개의 값을 읽기 위하여 for문을 사용하여 값을 읽습니다.
# 8. line.strip()은 줄 마지막에 줄바꿈 문자를 삭제합니다.