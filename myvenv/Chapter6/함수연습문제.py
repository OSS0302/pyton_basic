# def printSumAvg(x,y,z):
#     sum =x+y+z
#     avg =sum/3
#     print(f"합계:{sum} 평균:{int(avg)}")
# printSumAvg(10,20,30)

import random

def getrandomNumber():
    number = random.randint(1,45)
    return number

lotto = []
for i in range(6):
    if i not in lotto:
        lotto.sort()
        lotto.append(getrandomNumber())
        
print(lotto)

# 중복 가능
import random

def getrandomNumber():
    number = random.randint(1,45)
    return number
lotto_num=[]# 로또 번호를 리스트에 저장
count =0 #현재 뽑은 숫자 갯수
while True:
    if count >5:
        break
    random_num = getrandomNumber()
    if random_num not in lotto_num:
        lotto_num.append(random_num)
        count +=1
lotto_num.sort()
for num in lotto_num:
    print(num, end=" ")
