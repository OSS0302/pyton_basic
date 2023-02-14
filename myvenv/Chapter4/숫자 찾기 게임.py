# 먼저 컴퓨터가 1 에서 100까지 중 임의의 숫자를 생성한다.
# 다음 으로 사용자가 추측하는 숫자를 입력하면 컴퓨터가 생성한 임의 숫자보다 큰지 ,작은지를 계속 비교해준다.
# 기회는 5번 계속하다가 맞히면 정답입니다. 입력한 숫자는 n입니다 를 출력한다.
# 기회 추가하기 
import random
chance = int(input("기회를 입력해주세요"))
ramdom_num = random.randint(1,100)
print(ramdom_num)
count = 0
for i in range(1,chance+1):
    user  = int(input("숫자를 맞혀주세요"))
    count+=1
    if ramdom_num == user:
        print(f"정답입니다입력한 숫자는{ramdom_num}입니다.")
        break
    elif user < ramdom_num:
        print("숫자가 너무 작습니다.")
    elif user > ramdom_num:
        print("숫자가 너무 큽니다.")




