language = ["사랑해","고마워","부탁해","행복해","치킨무"]
print("Let's Learning Korean")
count =0
for word in language:
    print(word)
    korea=input()
    if word == korea:
        count +=1
        continue
    else:
        break

print("전체 문제갯수",len(language))
print("맞친 문제갯수",count)
print("틀린 문제갯수",len(language)-count)
    # 갯수 추가하기
# 전체 문제 개수: 4 개
# 맞힌 문제 개수: 2 개
# 틀린 문제 개수: 2 개


   
        
    