# 클래스를 사용하는  이유

# 클래스를 사용하지 않았다면 
champion1_name = "이즈리엘"
champion1_health = 700
champion1_attack = 90
print(f"{champion1_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion2_name = "리신"
champion2_health = 800
champion2_attack = 90
print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name,attack):
    print(f"{name} 기본공격{attack}")

basic_attack(champion1_name,champion1_attack)
basic_attack(champion2_name,champion2_attack)

print("========클래스를 사용한 경우===============")

class champion:
    def __init__(self,name,health,attack):
        self.name = name
        self.health =health
        self.attack =attack
        print(f"{name}님 소환사의 협곡에 오신것을 환영합니다.")
    def basic_attack(self):
        print(f"{self.name} 기본공격{self.attack}")
ezreal= champion("이즈리엘",700,90)
leesin= champion("리신",800,95)
timo= champion("티모",800,50)

ezreal.basic_attack()
leesin.basic_attack()
timo.basic_attack()        