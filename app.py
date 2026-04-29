class Rarity:
    def __init__(self,common,uncommon,rare,epic,legendary):
        self.common=common
        self.uncommon=uncommon
        self.rare=rare
        self.epic=epic
        self.legendary=legendary
    def damage(self,damage,common,uncommon,rare,epic,legendary):
        


class Villain(Rarity):
    def __init__(self,name,level,weapon,armor,health):
        self.name=name
        self.level=level
        self.weapon=weapon
        self.armor=armor
        self.health=health

    def weaponstats(self,weapon,damage):
        