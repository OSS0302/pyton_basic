# 부모 자식 클래스

class Player():
     def __init__(self, nickname , mineral,gas, unit_list):
        self.name = nickname
        self.mineral =mineral
        self.gas = gas
        self.unit_list = unit_list

class unit_list():
    def __init__(self, name , health,shield, attack):
        self.name = name
        self.health =health
        self.shield = shield
        self.attack = attack

# class unit_info(Player):



