#조건 문제2
# 조건) 10시간 이상 : 휴대폰 잠금 해제, 5시간 이상 : 휴대폰 30분 사용가능, 나머지 : 사용불가능

study_time = int(input("공부시간을 입력하세요>>"))

if study_time >= 10:
    print("휴대폰이 잠금이 헤제됩니다.")
elif study_time >= 5:
    print("휴대폰이 30분간 사용 가능합니다.")
else:
    print("휴대폰 사용이 불가능합니다.")