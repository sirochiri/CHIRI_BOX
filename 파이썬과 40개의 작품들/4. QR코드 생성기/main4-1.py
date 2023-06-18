import qrcode

qr_Data = 'www.naver.com'
qr_img = qrcode.make(qr_Data)

save_path = '4. QR코드 생성기\\' + qr_Data + '.png'
qr_img.save(save_path)



# 1. qrcode 라이브러리를 불러옵니다
# 3. qr_data변수에 'www.naver.com' 문자열을 바인딩 합니다.
# 4. qrcode.make로 이미지를 만들어 qr_img 변수에 바인딩 합니다.
# 6. save_path변수에 저장될 경로를 바인딩 합니다. 
#    [4. QR코드 생성기] 폴더에 wwww.naver.com.png 로 저장됩니다.
# 7. 이미지를 저장합니다.ㅌ