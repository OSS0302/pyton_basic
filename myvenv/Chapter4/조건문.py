# 조건문 
# 조건에 따라 실행 할 명령이 달라지는것
id  = input("아이디를 입력해주세요")
nickname= "kim88"
PassWord = "1234" # 패스워드
pw= input("비밀번호를 입력하세요>>>>")
if PassWord == pw and id == nickname :
    print("로그인성공")
elif(pw == ""):
    print("아무것도입력하지 않았습니다.")
else:
    print("로그인 실패 비밀번호를 다시입력해주세요")

