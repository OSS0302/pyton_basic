# 상속 
#클레스 들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용
# 부모클래스
class Monster:
    def __init__(self,name ,health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기 ")

# 자식 클래스
class Wolf(Monster):
    pass
class shark(Monster):
    def move(self): # 메서드 재정의하기  
        print(f"[{self.name}] 헤엄치기")
class dragon(Monster):
    def move(self): # 메서드 재정의하기 
        print(f"[{self.name}]날기")

wolf = Wolf("울프",1400, 300)
wolf.move()

shark = shark("상어",1200, 500)
shark.move()

dragon = dragon("드래곤",8000, 300)
dragon.move()
    
