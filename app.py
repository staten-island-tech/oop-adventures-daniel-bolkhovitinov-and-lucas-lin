import random
class placeholderheroidk:
    def __init__(self,name,money,weapon,health):
        self.name=name
        self.money=money
        self.weapon=weapon
        self.health=health

class Villain:
    def __init__(self,name,weapon,money,power,hp):
        self.name=name
        self.__money=money
        self.power=power
        self.__hp=hp
        self.__weapon=weapon
        
    def weaponattack(self,damage):
        print(f"{self.__weapon} has done {damage} damage!")

    def summoned(self,__name):
        print(f"{self.name} has summoned {__name}")

    def gettingattacked(self):
        attacked = random.randint(20,30)
        print(f"heroname has done {attacked} damage to {self.name} and {Monsterdict['_Monster__name']}")
        self.__hp -= attacked
        Monsterdict['hp'] -= attacked
        print(f"{self.name} health is now {self.__hp}!")
        print(f"{Monsterdict['_Monster__name']} health is now {Monsterdict['hp']}!")
    
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
            print(f"{self.name} has been defeated.{self.name} has dropped {self.__money} money and dropped {self.__weapon}")



class Monster(Villain): 
    def __init__(self, name, money,power,hp):
        self.__name = name
        self.money = money
        self.power = power
        self.hp = hp

    def attack(power,self):
        damage=random.randint(50,100)
        print(f"{Monsterdict['_Monster__name']} with {Monsterdict['power']} has done {damage} damage!")

    def block(self):
        heroattack=int(50)
        dmgreduction=heroattack/2
        print(f"{self.__name} has blocked your attack by {dmgreduction} damage!")
    
class dungeon(Villain):
    def __init__(self,name,room):
        self.name=name
        self.room=room
    
    def entryroom(self):
        dungeon_responses = {
                1: "Then there’s no turning back now.",
                2: "Stay close. These halls aren’t forgiving.",
                3: "Keep your weapon ready and your eyes open.",
                4: "What ever happens, don’t get separated.",
                5: "Alright… let’s see what’s waiting for us inside."
                }
        print(f"You have entered into {self.name} dungeon.")
        
        decision=input("Do You Wish to Continue In? Yes/No: ")
        
        if  decision == ("no"):
            print("You Have No Choice get yo sorry ass in there lol")
            health = 100
            damaged =  health/2 
            print(f"Your health has fallen by {damaged} health")
        elif decision == ("yes"):
            randomline=random.randint(1,5)
            print(dungeon_responses[randomline])
    def bridgeroom(self):
        print("A bridge lays between you and venturing farther into the dungeon.The bridge groaned beneath the weight of the wind, its broken planks swaying above the dark ravine below.")
        bridge=input(f"Do You Wish To cross the bridge and make it to the boss faster, or find a different route?")
        if bridge == ("yes"): #need to make it accept more inputs
            chance = random.randint(1,4)
            if chance == 1:
                print("Your footing slips on the rotten planks, and within seconds you vanish into the abyss below, never to rise again.")
                # they die instantly or lose health idk we can put the code in later
            elif chance >= 2:
                print("You have crossed the bridge safely, and explore deeper into the dungeon")
        elif bridge == ("no"):#need to make it accept more inputs
            print("you have left the room, but tripped and dropped your sword into the ravine, never to be seen again")#could add something to do this later
    
    def traproom(self):
        survival_choices = {
           "option":"Jump as high as you can, and hang on the ceiling pipe",
           "option": "run as fast as you can into the crack",
           "option":"use your items and body weight to hold the walls in place"
        }
        print("you walked in the blank room, and saw nothing, but then, hidden mechanisms clicked to life around them")
        print("the chamber was a trap room, and the doors slammed shut behind them")
        print("as the walls close in on you, you see a crevice on the wall for survival, and see a pipe on the ceiling.Do You")
        for index,item in enumerate(survival_choices):
            print(index, ":",item["option"] )

     
Kingsley = Monster("Kingsley",1000,"MindlessCrashouts",80)
Monsterdict=Kingsley.__dict__

Goyco = Villain("Goyco","Textbook",100,"summons",200)
Villaindict=Goyco.__dict__

arbys =dungeon("Arbys",10)

""" Goyco.weaponattack(50)
Goyco.summoned(idk['_Monster__name'])
Kingsley.attack(idk['power'])
Goyco.gettingattacked()
Goyco.dialogue()
Kingsley.block() """


arbys.traproom()