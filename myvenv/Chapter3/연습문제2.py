year = int(input("태어난 연도를 입력하세요>>>"))
age = 2023 -year
print(f"나이는",age,"입니다.")

# 생년월일 ->나이구하기 
age_born = int(input("나이를 입력해주세요"))
born_year = 2023- age_born
print(f"생년월일{born_year}년입니다") 

if age <=26 and age >=20:
    print("대학생")
elif age <20 and age>=17:
    print("고등학생이다.")
elif age < 17  and age >=14:
    print("중학생")
elif age < 14 and age >=8:
    print("초등학생")
else: 
    print("학생이 아닙니다.") 
    