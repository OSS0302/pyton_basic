# 딕셔너리
stock_a = {"삼성전자":82000, "LG전자": 15000}

stock_b={

"삼성전자":[85000,81500,81500,8200],
"LG전자":(150000,149000,148000,151000,152000)

}
stock_c ={
    "삼성전자":{
        "현재가":82000,
        "보유수량":5,
        "매수단가": 81000
    }

}
print(stock_a)
print(stock_b)
print(stock_c)

#딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

#딕셔너리 할당하기 
stock_a["심성전자"]= 85000
print(stock_a)
# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)
# 딕셔너리함수
stock_d = {
    "삼성전자" :82000,
    "sk하이닉스" :123000,
    "네이버" :370000,
    "카카오" : 133000
}
# item() : 키와 데이터쌍
for item in stock_d.items():
    print(item) #  키와 데이터 둘다 출력
    print(item[0]) # 키만 출력하기
    print(item[1]) # 데이터만 출력하기

#keys( ): 키
for key in stock_d.keys():
    print(key)

#value( ): 데이터
for values in stock_d.values():
    print(values)


