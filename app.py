import random
class Villain:
    def __init__(self,villainname,weapon,money,power,hp):
        self.villainname=villainname
        self.money=money
        self.power=power
        self.hp=hp
        self.__weapon=weapon
        villainname=object

    def weaponattack(self,damage):
        print(f"{self.__weapon} has done {damage} damage!")

    def summoned(self,__name):
        print(f"{self.villainname} has summoned {__name}")

class Monster(Villain): 
    def __init__(self, name, money,power,hp):
        self.__name = name
        self.money = money
        self.power = power
        self.hp = hp

<<<<<<< Updated upstream
=======
    def summoned(self,__name):
        super().__init__(villainname="Goyco")
        print(f"{self.villainname} has summoned {__name}")

>>>>>>> Stashed changes
    def attack(power, self):
        self.power.append()
        print(f"{self.hp} has %{self.__hp}")
        
        
Kingsley = Monster("Kingsley",1000,"MindlessCrashouts",80)
idk=Kingsley.__dict__

Goyco = Villain("Goyco","Textbook",0,"summons",200)

Goyco.weaponattack(50)
<<<<<<< Updated upstream
Goyco.summoned(idk['_Monster__name'])
=======
Kingsley.summoned(Kingsley)
>>>>>>> Stashed changes

        