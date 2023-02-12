# 상속 
#클레스 들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용

# 클래스 변수 
#: 인스턴스들이 모두 공유하는 변수
# 부모클래스
class Monster:
    max_num =1000
    def __init__(self,name ,health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기 ")
import random
# 자식 클래스
class Wolf(Monster):
    pass
class shark(Monster):
    def move(self): # 메서드 재정의하기  
        print(f"[{self.name}] 헤엄치기")
class dragon(Monster):
    # 생성자 오버라이딩 
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills =("불뿜기","꼬리치기","날개치기")
    def move(self): # 메서드 재정의하기 
        print(f"[{self.name}]날기")
    def skill(self):
        print(f"[{self.name}]스킬 사용{self.skills[random.randint(0,2)]}")
    
        

wolf = Wolf("울프",1400, 300)
wolf.move()
print(wolf.max_num)
shark = shark("상어",1200, 500)
shark.move()
print(shark.max_num)
dragon = dragon("드래곤",8000, 900)
dragon.move()
dragon.skill()
print(dragon.max_num)