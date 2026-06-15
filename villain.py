import random
import time
import json
with open("weapons.json", "r") as file:
    weapons_data = json.load(file)
    weapons = weapons_data["weapons"]
randomnumber = random.randint(0, len(weapons)-1)
randomweapon=weapons[randomnumber]["name"]
randomweapondmg = int(weapons[randomnumber]["attack"])
class hero:
    def __init__(self,name,money,weapon,health,damage):
        self.name=name
        self.money=money
        self.weapon=weapon
        self.health=health
        self.damage=damage
lebronjames = hero("name",random.randint(10,30), randomweapon, random.randint(150,200),randomweapondmg)
lebron=lebronjames.__dict__
heroname = lebronjames.name
heroweapon = lebronjames.weapon
herohealth = lebronjames.health
heromoney = lebronjames.money
herodamage = lebronjames.damage

class Villain:
    def __init__(self,name,weapon,money,power,hp):
        self.name=name
        self.__money=money
        self.power=power
        self.__hp=hp
        self.__weapon=weapon
        
    def weaponattack(self):
        while self.__hp > 0:
            damage = random.randint(10,30)
            print(f"{self.__weapon} has done {damage} damage!")
            break

    def summoned(self,__name):
        print(f"{self.name} has summoned {__name}!")

    def gettingattacked(self):
        lebronjames = hero(name,random.randint(1,100), randomweapon, random.randint(100,200),randomweapondmg)
        attacked = lebronjames.damage
        print(f"{name} has done {attacked} damage to {self.name}")
        self.__hp -= attacked
        print(f"{self.name} health is now {self.__hp}!")
        
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
            print(f"{self.name} has been defeated.{self.name} has dropped {self.__money} money and dropped {self.__weapon}!")
            print(f"You have defeated {self.name}!")
            time.sleep(1)
            print("You escaped the dungeon and became a legend!")
            time.sleep(1)
            print("YOU WIN!")
            exit()