import random
class Villain:
    def __init__(self,villainname,weapon,money,power,hp):
        self.villainname=villainname
        self.__money=money
        self.power=power
        self.__hp=hp
        self.__weapon=weapon
        

    def weaponattack(self,damage):
        print(f"{self.__weapon} has done {damage} damage!")

    def summoned(self,__name):
        print(f"{self.villainname} has summoned {__name}")

    def powerattack(self):
        damage=random.randint(50,100)
        print(f"{idk['_Monster__name']} with {idk['power']} has done {damage} damage!")

    def gettingattacked(self):
        attacked = random.randint(20,30)
        print(f"heroname has done {attacked} damage to {self.villainname}")
        self.__hp -= attacked
        print(f"{self.villainname} health is now {self.__hp}!")

        if self.__hp == 0:
            print(f"{self.villainname} has been defeated.{self.villainname}has dropped{}")


class Monster(Villain): 
    def __init__(self, name, money,power,hp):
        self.__name = name
        self.money = money
        self.power = power
        self.hp = hp

    def attack(power, self):
        self.power.append()
        print(f"{self.hp} has %{self.__hp}")
        
        
Kingsley = Monster("Kingsley",1000,"MindlessCrashouts",80)
idk=Kingsley.__dict__

Goyco = Villain("Goyco","Textbook",100,"summons",200)

Goyco.weaponattack(50)
Goyco.summoned(idk['_Monster__name'])
Goyco.powerattack()
Goyco.gettingattacked()
        