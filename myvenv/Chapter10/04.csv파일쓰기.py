# 파일쓰기
import csv

data = [
    ["name, class , class_number"],
    ["재석",1,1],
    ["준하",2,2],
    ["홍철",3,3],
    ["하하",4,4],
    ["형돈",5,60],
    ["명수",6,60]

]
file = open("./myvenv/Chapter10/student_info.csv","w",newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)
file.close()