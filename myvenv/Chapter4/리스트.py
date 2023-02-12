# #리스트 만들기

# # food_list = ["김치", "삼겹살", "밥", "목살", "…","된장찌게"]

# # 빈 리스트 만들기
# empty = []

# #데이터 추가하기
# a =[1,2,3]
# a.append(4)
# print(a)
# # 리스트 할당하기 
# print(a[0]) 
# print(a[1]) 
# print(a[2]) 
# # 리스트 삭제하기 
# del a[3]
# print(a)

#  # 데이터 슬라이싱 
# b = [3,4,2,1]
# print(b[1:4])# 인덱스 1 ~3까지 
# # 데이터 길이
# print(len(b))
# # 리스트 정렬
# print(b)
# b.sort()
# print(b)

#데이터 슬라이싱
food_list = ["김치", "삼겹살", "밥", "목살", "…","된장찌게"]
# - 리스트 슬라이싱
print(food_list[1:4]) #1에서 4까지나온다.
print(food_list[:])# 전체
print(food_list[1:]) #인덱스 1번부터 나온다.
print(food_list[:3]) # 인덱스 3까지 나온다.

result=[33,40,12,63,52]

#데이터 축가하기 
result.append(9)
print(result)