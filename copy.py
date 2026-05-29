import random
import time
import json
with open("weapons.json", "r") as file:
    weapons_data = json.load(file)
    weapons = weapons_data["weapons"]
class hero:
    def __init__(self,name,money,weapon,health):
        self.name=name
        self.money=money
        self.weapon=weapon
        self.health=health    
        
class inventory:
    def __init__(self,item):
        self.item=item
    def update_items(self,item_id,amount):
        self.items[item_id].quantity+=amount
        print(f"Updated {self.items[item_id].name} stock by {amount}.")
class Villain:
    def __init__(self,name,weapon,money,power,hp):
        self.name=name
        self.__money=money
        self.power=power
        self.__hp=hp
        self.__weapon=weapon
        
    def weaponattack(self):
        while self.__hp > 0:
            damage = 20
            print(f"{self.__weapon} has done {damage} damage!")
            break

    def summoned(self,__name):
        print(f"{self.name} has summoned {__name}!")

    def gettingattacked(self):
        attacked = random.randint(20,30)
        print(f"heroname has done {attacked} damage to {self.name}")
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



class Monster(Villain): 
    def __init__(self, name, money,power,damage,hp):
        self.__name = name
        self.money = money
        self.power = power
        self.hp = hp
        self.damage = damage

    def attack(power,self):
        damage=random.randint(50,100)
        print(f"{Monsterdict['_Monster__name']} with {Monsterdict['power']} has done {damage} damage!")

    def block(self):
        while True:
            randomblockchance = random.randint(1,2)
            break
        heroattack=int(50)
        if randomblockchance == 1:
            dmgreduction=heroattack/2
            print(f"{self.__name} has blocked your attack by {dmgreduction} damage!")
        elif randomblockchance == 2:
            self.hp -= heroattack
            print(f"{self.__name} has took {heroattack} damage!")
        if self.hp <= 0:
            print(f"You Have killed {Monsterdict['_Monster__name']}")
    
class dungeon(hero):
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
            print("You Have No Choice get yo sorry ahh in there lol")
            health = 100
            damaged =  health/2 
            print(f"Your health has fallen by {damaged} health")
        elif decision == ("yes"):
            randomline=random.randint(1,5)
            print(dungeon_responses[randomline])
    def bridgeroom(self): 
        print("A bridge lays between you and venturing farther into the dungeon.The bridge groaned beneath the weight of the wind, its broken planks swaying above the dark ravine below.")
        bridge=input(f"Do You Wish To cross the bridge and make it to the boss faster, or find a different route?").lower()
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
        survival_choices = [
           {"name":"Jump as high as you can, and hang on the ceiling pipe"},
           {"name": "run as fast as you can into the crack"},
           {"name":"use your items and body weight to hold the walls in place"},
        ]
           
        print("You walked in the blank room, and saw nothing, but then, hidden mechanisms clicked to life around them")
        time.sleep(1)
        print("The chamber was a trap room, and the doors slammed shut behind them")
        time.sleep(1)
        print("As the walls close in on you, you see a crevice on the wall for survival, and see a pipe on the ceiling. Do You")
        
        for index,items in enumerate(survival_choices):
            print(index, ":", items["name"])

        choice = int(input("What Do you want to do? Pick the number to choose your choice:"))

        if choice == 0:
            survival =random.randint(1,10)
            if survival  == 1:
                print("You jump towards the pipe and hang on to it. As the walls close in, you hang on with dear life and manage to make it out from a vent hidden in the ceiling.")
            else :
                print("You jump up, but your hands slip and you fall and you die")
        elif choice == 1:
            survivalpt2 = random.randint(1,3)
            if survivalpt2 ==  1:
                print("You run as fast as you can, and squeezed in the hole. As the walls contract, you see gold appear from the floor.")
            else : # change later
                print("You run as fast as you can, but then, you trip and die")
        elif choice == 2:
            survivalpt3  = random.randint(1,100)
            if survivalpt3 == 1:
                print("As you brace your items and muscles against the walls, you suddenly spike in aderinline and coristol, giving you immense strength untill the walls contract. As you passout, gold and jewels fall from the ceiling")
            else : # change later
                print("As you brace yourself, you withstand your body, against the forces of the walls")
                time.sleep(2)
                print("But then, out of nowhere, your spine snaps, causing you to pass out and die ")

    def fightroom(self): # almost done, will do later
        fight_choices = [
            {"option": "Fight"},
            {"option": "Items"},
            {"option": "Run"}
        ]
        orc_hp = [
            {"name":"Rattlefang","health":50},
            {"name":"Murkbit","health": 55},
            {"name":"Skarnox","health": 45}
        ]
        Kingsley = Monster("kingsley",1000,"MindlessCrashouts",50,80)
        print("As you walk in, you come across foul creatures ready to fight you")
        time.sleep(1)
        heroname = lebron['name']
        heroweapon = lebron['weapon']
        herohealth = lebron['health']
        countdown = 3
        orcdmg = random.randint(6,8)
        print(f"As you grip your {heroweapon} tightly, the room lights up, showing a group of orcs ready to kill you {heroname}.")
        time.sleep(1)
        print(f"You then see {Monsterdict['_Monster__name']} show up, ready to kill you")
        time.sleep(1)
        while True:
            for index, items in enumerate(fight_choices):
                print(index, ":", items["option"])
            for items in orc_hp:
                print(f"Orc: {items['name']} hp: {items['health']}")
            print(f"Monster: {Monsterdict["_Monster__name"]}, hp:{Monsterdict["hp"]}")
            heroweapondmg = random.randint(60,70)# fixed value later
            choice = int(input("What Will You Do? Type number for option: ")) #inventory not made so items dont work 
            if choice == 0:
                fight = input("Who are you attacking? Type name to decide: ").lower() #health is fixed, doesnt change in text at all
                if fight == ("rattlefang"): #babyproof later
                    orc_hp[0]["health"] -= heroweapondmg
                    print(f"{orc_hp[0]["name"]} is now at {orc_hp[0]["health"]} health!")
                elif fight == "murkbit":
                    orc_hp[1]["health"] -= heroweapondmg
                    print(f"{orc_hp[1]["name"]} is now at {orc_hp[1]["health"]} health!")
                elif fight == "skarnox":
                    orc_hp[2]["health"] -= heroweapondmg
                    print(f"{orc_hp[2]["name"]} is now at {orc_hp[2]["health"]} health!")
                elif fight == Monsterdict["_Monster__name"]:
                    Monsterdict["hp"] -= heroweapondmg
                    print(f"{Monsterdict['_Monster__name']} is now at {Monsterdict['hp']} health")
                
                else :
                    print("Try Again")
                    continue
            if choice == 1:
                print("Your bag has nothing because you dropped it when you tripped")
            if choice == 2:
                Runaway = random.randint(1,10)
                if Runaway >= 8:
                    print("You escaped the room, and ran away")
                    break
                elif Runaway <= 8:
                    print("You tried to run, but failed")
            
            livingorc = [orc for orc in orc_hp if orc["health"] > 0]
            if livingorc:
                randomorc = random.choice(livingorc)
                herohealth -= orcdmg
                print(f"{randomorc["name"]} damaged you by {orcdmg}")
                print(f"You are now at {herohealth} health!")
           
            for orc in orc_hp:
                if orc["health"] <= 0:
                    print(f"You have killed {orc['name']}.")
            
            if all(orc["health"] <= 0 for orc in orc_hp) and Monsterdict['hp'] <= 0:
                print("All orcs are dead!")
                break

            countdown -= 1
            print(f"{Monsterdict['_Monster__name']} will attack you in {countdown} turns")
            
            if herohealth <= 0:
                print("You Have Died")

            if countdown == 0:
                    Kingsley.attack(self)
                    countdown += 3
            if Monsterdict["hp"] <= 0:
                    print(f"You have killed {Monsterdict['_Monster__name']}.")
                    countdown == -1
                    
    def bossroom(self): #also mostly done, will need to add death and inventory, and end it here because this is last room
        fight_choices = [
            {"option": "Fight"},
            {"option": "Items"}
        ]
        countdown = 3
        print("As you walk into the room, you see it.")
        time.sleep(1)
        print("You see a massive shadow, from the distance.")
        time.sleep(1)
        Goyco = Villain("goyco","Textbook",100,"summons",200)
        Villaindict=Goyco.__dict__
        Kingsley = Monster("kingsley",1000,"MindlessCrashouts",50,80)
        Monsterdict=Kingsley.__dict__
        print(f"You see it, {Villaindict['name']} ready to kill you")
        time.sleep(1)
        Goyco.summoned(Monsterdict['_Monster__name'])
        time.sleep(1)
        while True:
            for index, items in enumerate(fight_choices):
                print(index, ":", items["option"])
            choice = int(input("What will you do? Pick number for option:"))
            if choice == 0:
                whichone = input("Who do you choose to fight?").lower()
                if whichone == Villaindict['name']:
                    Goyco.gettingattacked()
                    Goyco.dialogue()
                elif whichone == Monsterdict['_Monster__name']:
                    Kingsley.block()
            if choice == 1:
                print("Nothing")#will do inventory soon
            
            Goyco.weaponattack()
            
            while Monsterdict['hp'] <= 0:
                countdown -= 1
                print(f"{Monsterdict['_Monster__name']} will attack you in {countdown} turns")
                if countdown == 0:
                    Kingsley.attack(self)
                    countdown += 3
                break
            

            
                
        



               
        
Kingsley = Monster("kingsley",1000,"MindlessCrashouts",50,80)
Monsterdict=Kingsley.__dict__

randomnumber = random.randint(1,20)
name = input("What is Your Name?")
randomweapon=weapons[randomnumber]["name"]
lebronjames = hero(name,random.randint(1,100), randomweapon, random.randint(100,200))
lebron=lebronjames.__dict__
print(lebron)
print(Monsterdict)

arbys=dungeon("Arbys",10)
""" 
arbys.fightroom() 
""" 
"""arbys.bossroom() """
