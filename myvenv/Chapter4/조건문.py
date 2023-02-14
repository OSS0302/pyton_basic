# 조건문 
# 조건에 따라 실행 할 명령이 달라지는것

PassWord = "1234" # 패스워드

user_input= input("비밀번호를 입력하세요>>>>")
if PassWord == user_input:
    print("로그인성공")
elif(user_input == ""):
    print("아무것도입력하지 않았습니다.")

else:
    print("로그인 실패 비밀번호를 다시입력해주세요")

