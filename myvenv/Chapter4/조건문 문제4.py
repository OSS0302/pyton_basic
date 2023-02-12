# 조건문제4)
# 국영수가 평균점수가 80점이상이면 합격 미만 이면 불합격 이상한점수 적으면 잘못입력되었습니다.
korea = int(input("국어점수를입력해주세요!>>"))
math =  int(input("수학점수를입력해주세요!>>"))
english = int(input("영어점수를입력해주세요!>>"))
avg_score = (korea+math+english)/3
# 방법1)
if ( korea <0 or korea> 100 or math <0 or math>100 or english <0 or english >100 ):
    print("점수를 잘못입력했습니다.")
elif(avg_score>=80):
    print("불합격")
elif(avg_score<=80):
    print("합격")

