class Monster:
    def say(self):
        print("i am monster!")

goblin = Monster()
goblin.say()

#파이썬에서는 자료형도 클래스다
a =10
b= "문자열객체"
c= True
# 문자열 객체 메서드를 알수있는방법
print(b.__dir__())