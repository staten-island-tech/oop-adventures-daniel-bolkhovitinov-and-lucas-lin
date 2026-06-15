import random
import time
import json
with open("weapons.json", "r") as file:
    weapons_data = json.load(file)
    weapons = weapons_data["weapons"]
randomnumber = random.randint(0, len(weapons)-1)
randomweapon=weapons[randomnumber]["name"]


class hero:
    def __init__(self,name,money,weapon,health,damage):
        self.name=name
        self.money=money
        self.weapon=weapon
        self.health=health
        self.damage=damage
    def weaponpowerup(self):
        maxpower = 0 
        while True:
            weaponpowerup = input("Do You Want to level your weapon damage up for 20$? Yes/No:").lower()
            if weaponpowerup == ("yes"):
                self.damage += 6
                self.money -= 20
                maxpower += 1
                if self.money <= 9:
                    break
                if maxpower == 3:
                    print("Ran out of powerups")
                    break
                print("Upgraded weapon dmg by 6")
                print("Took 10$ away!")
                print(f"You Now Have {self.money} money now")
            if weaponpowerup == ("no"):
                print("Brokie")
                break
    def weaponpowerupbutexpensive(self):
        maxpower = 0 
        while True:
            weaponpowerup = input("Do You Want to level your weapon damage up for 60$? Yes/No:").lower()
            if weaponpowerup == ("yes"):
                self.damage += 8
                self.money -=60
                maxpower += 1
                if self.money <= 59:
                    break
                if maxpower == 3:
                    print("Ran out of powerups")
                    break
                print("Upgraded weapon dmg by 8")
                print("Took 60$ away!")
                print(f"You Now Have {self.money} money now")
            if weaponpowerup == ("no"):
                print("Brokie")
                break
    def heal(self, amount):
        self.health += amount
        print(f"You healed {amount} HP!")
        print(f"Current HP: {self.health}")
randomweapondmg = int(weapons[randomnumber]["attack"])