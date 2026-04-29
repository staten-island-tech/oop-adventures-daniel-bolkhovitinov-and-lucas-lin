class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Josh = Hero("Jillian", 150, ["Potion"])
Josh.buy({"title": "Sword", "atk": 34})
print(Josh.__dict__)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}") 

class Monster: 
    def __init__(self, name, money,power,hp):
        self.name = name
        self.money = money
        self.power = power
        self.hp = hp
    def attack(power, self):
        self.power.append()
        print(f"{self.hp} has %{self.__hp}")

Whalen = Monster("Whalen", 150, 100 ["Brute Strength"],50)
Whalen.attack("title": "Brute Attack","atk":150)
print(Whalen.__dict__)