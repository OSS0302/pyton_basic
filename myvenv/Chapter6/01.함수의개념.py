# #함수를 사용하는 경우

# #함수를 사용하지 않는경우
# print("안녕하세요.동준님")
# print("현재 프리미엄 서비스 사용기간이 30일 남았습니다.")
# print("안녕하세요.현식 님")
# print("현재 프리미엄 서비스 사용기간이 15일 남았습니다.")
# print("안녕하세요.원준님")
# print("현재 프리미엄 서비스 사용기간이 7일 남았습니다.")
# print("===========================================")
# #함수를 사용한 경우
# def printMessage(name , date):
#     print("안녕하세요.",name,"님")
#     print("현재 프리미엄 서비스 사용기간이",date,"일 남았습니다.")
# printMessage("김의준",30)
# printMessage("허영우",20)
# printMessage("황상하",10)

# #정의하기
# def printHello():
#     print("Hello")
# #호출하기    
# printHello()

#매개 변수가있는 함수
# #정의하기 
# def sum(a,b):
#     print(a+b)
# sum(6,4)

#반환값이 있는경우
# import random
# #정의하기
# def getRamdomNumber(): # def함수이름():
#     number =random.randint(1,10) #명령블록
#     return number # return 반환값
# #호출하기
# print(getRamdomNumber())


#매개변수와 반환값이 있는경우
#정의하기 
def sum(a,b):
    result =a+b
    return result
#호출하기
print(sum(6,6))