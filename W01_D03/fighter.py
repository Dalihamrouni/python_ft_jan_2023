from character import Character

class Fighter(Character):
    # Constractor
    def __init__(self,name ,weapon):
        super().__init__(name) # Constarctor of the parent class
        self.name = name 
        self.strength = 100  #! Poylorphism ==>  Modification of the Parent Attribute
        self.defense = 30    #! Poylorphism ==>  Modification of the Parent Attribute
        self.weapon = weapon #! Poylorphism ==> Creation of a new attribute specific to the child class
