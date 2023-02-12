# 튜플
# 일기 전용 리스트
a =(3,3,4,6)
b =3,3,4,6
# 튜플은 가로가 생략 가능하다
c=(3,) #튜플 한개를 쓸 경우에 뒤에 콤마를 쓴다.
d= 3, # 튜플 한개도 가로 생략 가능하다
e= tuple([3,4,5]) #튜플을 리스트로 만들수있다.
f= list(range(10))# 리스트 안에 range객체를 쓸 수있다.
g= tuple(f) # 리스트를 tuple 로 바꿀수있다.

h=3,4,5
i =list(h)

# 튜플 관련 함수
x = 5,6,7,8,6,6
print(sum(x)) # 합계
print(max(x)) # 최댓값
print(min(x)) # 최솟값
print((x.count(6))) # 갯수
print(x.index(7)) # 인덱스