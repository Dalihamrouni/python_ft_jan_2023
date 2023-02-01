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


# maxi = Character("Max")
# maxi.display_infos()

# ! Inheritance
class Fighter(Character):
    # Constractor
    def __init__(self,name ,weapon):
        super().__init__(name) # Constarctor of the parent class
        self.name = name 
        self.strength = 100  #! Poylorphism ==>  Modification of the Parent Attribute
        self.defense = 30    #! Poylorphism ==>  Modification of the Parent Attribute
        self.weapon = weapon #! Poylorphism ==> Creation of a new attribute specific to the child class

class Sorssor(Fighter):
    def __init__(self,name, weapon):
        super().__init__(name , weapon)

alex = Fighter("Alex", "Knife")

# alex.display_infos()
# print(alex.weapon)
hisoka = Sorssor("Hisoka", "Magic")
# hisoka.display_infos()

# !Abstraction

class Master:
    def __init__(self, name):
        self.name = name
        self.type = Fighter(name,"Sword") #! Abstraction

master = Master("Master_1")
master.type.display_infos()
