#파일 읽기
import csv
file = open("./myvenv/Chapter10/student_info.csv","r", encoding="utf-8-sig")
reader = csv.reader(file)
for data in reader:
    print(data)
file.close()