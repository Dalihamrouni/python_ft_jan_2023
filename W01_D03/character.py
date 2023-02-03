class Character:
    # Constractor
    # -Instance Metrhod
    def __init__(self,name):
        self.name = name
        self.strength = 50
        self.health = 100
        self.level = 1
        self.skills = 1
        self.intelligence = 10
        self.defense = 10
    
    # Instance Method
    def attack(self, target):
        target.health-= self.strength
        return self
    
    # Instance Method
    def defend(self, damage):
        damage-=self.defense
        self.health-=damage
        return self
    
    # Static Method
    def display_infos(self):
        print(f"{self.name} \n Level = {self.level} \n Skills = {self.skills} \n Health = {self.health} \n Intell = {self.intelligence} \n Defense = {self.defense}" )
