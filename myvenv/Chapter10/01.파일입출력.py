# 파일 쓰기 
file = open("./myvenv/Chapter10/data.txt","w" ,encoding ="utf8")
file.write("1.스타트 코딩과 함께하는 파이썬공부")
file.close()

#2. 파일추가 (이어쓰기)
file = open("./myvenv/Chapter10/data.txt","a" ,encoding ="utf8")
file.write("\n2.비전공자도 정말 쉽게 배울수있습니다.")
file.close()

# 파일 읽기 (읽기)
file = open("./myvenv/Chapter10/data.txt","r" ,encoding ="utf8")

# 3-1 파일 전체 읽기
data = file.read()
print(data)
file.close()

#3-2 파일 한줄 읽기
import readline
while True:
    data = file.readline()
    print(data ,end="")
    if data =="":
        break
file.close()
#프린트 함수 가 줄바꿈 되기 때문에 