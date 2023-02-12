# 생성자 
# : 인스턴스를 만들때 호출 되는 메서드

# 


class Monster :
    def __init__ (self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed
    def decrease_health(self,num):
        self.health -=num
    def get_health(self):
        return self.health
# 고블린과 울프 인스턴스 생성
gobiln = Monster(800,100,200)
gobiln.decrease_health(100)
print(gobiln.get_health())
# 늑대 인스턴스 생성

wolf = Monster(700, 150,400)
wolf.decrease_health(200)
print(wolf.get_health())