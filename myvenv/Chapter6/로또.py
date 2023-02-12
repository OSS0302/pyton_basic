# 로또문제
import random # 모듈(랜덤) 임포트하기 
def getramdomnumber():
    number = random.randint(1,45)
    return number

lotto_num = [] # 로또번호 넣어줄 빈리스트 생성
count =0 # 현재 뽑은 갯수
while True:
    if count>5:
        break
    random_num = getramdomnumber()
    if random_num not in lotto_num: # not in을 사용하면 in의 반대로 만든다.
        lotto_num.append(random_num)
        count +=1
lotto_num.sort() # 로또 번호 정렬
for num in lotto_num:
    print(num, end=" ")
