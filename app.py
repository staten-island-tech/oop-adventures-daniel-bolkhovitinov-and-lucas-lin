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
        damage=random.randint(1,10)
    def gettingattacked(self):
        attacked = random.randint(20,30)
        print(f"heroname has done {attacked} damage to {self.villainname}")
        self.__hp -= attacked
        print(f"{self.villainname} health is now {self.__hp}!")

        if self.__hp <= 0:
            print(f"{self.villainname} has been defeated.{self.villainname} has dropped {self.__money} money and dropped {self.__weapon}")

class Monster(Villain): 
    def __init__(self, name, money,power,hp):
        self.__name = name
        self.money = money
        self.power = power
        self.hp = hp

    def attack(power, self):
        super.__init__(Villain.powerattack)
        damage=random.randint(50,100)
        print(f"{idk['_Monster__name']} with {idk['power']} has done {damage} damage!")

class Goblin(Villain):
    def __init__(self,name,weapon,money,hp):
        super.__init__(money,hp)
        self.name=name
        self.weapon=weapon
        self.__money=money*3
        self.__hp=hp/2
        
    
    def check(__hp,__money):
        print(__hp)
        print(__money)
        
     
Kingsley = Monster("Kingsley",1000,"MindlessCrashouts",80)
idk=Kingsley.__dict__

Goyco = Villain("Goyco","Textbook",100,"summons",200)

Goblins = Goblin("Goblin",100,"dagger",50)

Goblins.check

Goyco.weaponattack(50)
Goyco.summoned(idk['_Monster__name'])
Kingsley.attack(idk['power'])
Goyco.gettingattacked()

