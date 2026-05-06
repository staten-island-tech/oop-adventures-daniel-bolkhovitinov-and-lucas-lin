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

    def gettingattacked(self):
        attacked = random.randint(20,30)
        print(f"heroname has done {attacked} damage to {self.villainname}")
        self.__hp -= attacked
        print(f"{self.villainname} health is now {self.__hp}!")
    def dialogue(self):
        villain_lines = {
        1: "You mistake mercy for weakness—that’s why you’re losing.",
        2: "I didn’t come this far to be stopped by someone like you.",
        3: "Every move you make… I’ve already accounted for it.",
        4: "Go on, fight harder. It only makes this more entertaining.",
        5: "You still believe you can win? How adorable.",
        6: "I am the consequence of every failure you tried to ignore.",
        7: "Hope is a fragile thing—I rather enjoy breaking it.",
        8: "You call this resistance? I call it delaying the inevitable.",
        9: "Kneel now, and I might let you watch the world fall.",
        10: "All your strength, and yet you’re still not enough.",
        11: "Heroes always cling to rules—that’s why they die.",
        12: "I’ve already taken everything from you… you just don’t realize it yet.",
        13: "This is the part where you understand how powerless you truly are.",
        14: "Struggle if you must. It won’t change the ending.",
        15: "In the end, they won’t remember you—they’ll remember me."
        }
        while self.__hp >= 1:
            randomlinechooser=random.randint(1,15)
            print(villain_lines[randomlinechooser])
            break
        
        if self.__hp <= 0:
            print(f"{self.villainname} has been defeated.{self.villainname} has dropped {self.__money} money and dropped {self.__weapon}")

class Monster(Villain): 
    def __init__(self, name, money,power,hp):
        self.__name = name
        self.money = money
        self.power = power
        self.hp = hp

    def attack(power,self):
        damage=random.randint(50,100)
        print(f"{idk['_Monster__name']} with {idk['power']} has done {damage} damage!")

    def block(self):
        heroattack=int(50)
        dmgreduction=heroattack/2
        print(f"{self.__name} has blocked your attack by {dmgreduction} damage!")

    


        
     
Kingsley = Monster("Kingsley",1000,"MindlessCrashouts",80)
idk=Kingsley.__dict__

Goyco = Villain("Goyco","Textbook",100,"summons",200)


Goyco.weaponattack(50)
Goyco.summoned(idk['_Monster__name'])
Kingsley.attack(idk['power'])
Goyco.gettingattacked()
Goyco.dialogue()
Kingsley.block()
