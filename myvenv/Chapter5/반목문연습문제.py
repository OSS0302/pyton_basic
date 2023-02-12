# 구구단


# for row in range(1):
#     for col in range(1,10):
#         print(gugudan,"*",col,"=",gugudan*col)
# gugudan = int(input("몇단을 출력할까요>>>")) # 구구단 행 입력함수받기

# while True:
#     gugudan = int(input("몇단을 출력할까요>>>")) # 구구단 행 입력함수받기
#     for row in range(1):
#         for col in range(1,10):
#             print(f"{gugudan}*{col}={gugudan*col}")

#while 문이용한 구구단 
gugudan = int(input("몇단을 출력할까요>>>")) # 구구단 행 입력함수받기
while True:
    i =1
    while i<10:
        print(f"{gugudan}*{i}={gugudan*i}")
        i+=1
        
    

