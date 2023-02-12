# # 연산 
# x = 5 
# y = 2 

# print( x+y) # 더하기
# print( x-y) # 빼기
# print( x*y) # 곱하기
# print( x/y) # 나누기
# print( x//y)# 몫
# print( x%y) #나머지
# print( x**y) # 제곱

# 문자열 연산 
tag1 = "프랑스"
tag2 = "잉글랜드"
tag3 = "포르투갈"
tag = tag1 + tag2 + tag3
print("문자열연산:",tag)

# message = "대한민국 2022년 카타르 월드컵에서 16강을 진출을 축하합니다.\n"*5 
# print(message)

# 복합 할당 연산자 
level = 10 #(level 1 증가)
level += 1 # level = level +1

health = 2000#( 체력 300 감소)
health += 200 # heath = health- 300

attack = 300 #(공격력 1.5 배 증가)
attack *= 1.5 #attack = attack * 1.5

speed = 240# (이동속도 50% 감소)
speed /= 2 # speed = spped/2

print(f" 레벨:{level},체력:{health}, 공격력:{attack}, 이동속도:{speed}")