#내장 모듈 
# : 파이썬 설치시 자동으로 설치되는모듈

from math import pi , ceil  as c # from 임포트 하면 다른이름 모듈이름을 정할수있다.
print(pi)
print(c(2.7))

#외부 모듈 
#: 다름 사람이 만든 파이썬 pip로 설치해서 사용
#pyautogui -> 자동으로 500,500 포인트로 2초 동안 움직여라 매크로 모듈
import pyautogui as pg
pg.moveTO(500, 500, duration=2)