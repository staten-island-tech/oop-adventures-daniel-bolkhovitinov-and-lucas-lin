
class Villain:
    def __init__(self,villainname,weapon,money,power,hp):
        self.villainname=villainname
        self.money=money
        self.power=power
        self.hp=hp
        self.__weapon=weapon

    def weaponattack(self,damage):
        print(f"{self.__weapon} has done {damage}")

    
class Monster(Villain): 
    def __init__(self, name, money,power,hp):
        self.__name = name
        self.money = money
        self.power = power
        self.hp = hp

    def summoned(self):
        super().__init__(villainname="Goyco")
        print(f"{self.villainname} has summoned {__name__}")

    def attack(power, self):
        self.power.append()
        print(f"{self.hp} has %{self.__hp}")
        
        
Kingsley = Monster("Kingsley",1000,"MindlessCrashouts",80)

Goyco = Villain("Goyco","Textbook",0,"summons",200)

Goyco.weaponattack(50)
Goyco.powersummon(Kingsley)

        