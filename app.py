
class Villain:
    def __init__(self,name,weapon,money,power,hp):
        self.name=name
        self.money=money
        self.power=power
        self.hp=hp
        self.__weapon=weapon

    def weaponattack(self,damage):
        self.__weapon += damage
        print(f"{self.__weapon} has done {damage}")

    def powersummon(self,Kingsley):
        print(f"{self.name} has summoned {Kingsley[self.name]}")


class Monster(Villain): 
    def __init__(self, name, money,power,hp):
        self.name = name
        self.money = money
        self.power = power
        self.hp = hp
    def attack(power, self):
        self.power.append()
        print(f"{self.hp} has %{self.__hp}")
        
        
Kingsley = Monster("Kingsley",1000,"MindlessCrashouts",80)

Goyco = Villain("Goyco","Textbook",0,"summons",200)

Goyco.weaponattack(50)
Goyco.powersummon()

        