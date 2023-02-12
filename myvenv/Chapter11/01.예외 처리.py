# 원화를 입력 , 환률 입력 -> 달러값

won =(input("원화 금액을 입력하세요"))
dollar =(input("환율을 입력 하세요"))

try: # 에외가 발생 할 수있는 코드
    print( int(won)/ int(dollar))
except ValueError as e: # 예외가 발생했을때 실행되는코드
    print(" 예외가 발생되엇습니다.",e)
except ZeroDivisionError as e:
    print("나누기 0은 불가능합니다.", e )
else: 
    print("예외가 발생 하지 않았을때 에도 실행되는 코드")
finally:# 파일 열고 닫기 해줄때 
    print("예외가 발생하던지 발생되지 않던지 항상 실행되는 코드")

# try: 셋트로 예외를 발생할수있는 부분을  감싸주면 더이상 프르그램 종료가 되지않는다.
# valueError :발생하는 에러 를 직접 지정 할 수있다. 
# valueError는 별칭을 쓸수있다.

#예외 만들기 
