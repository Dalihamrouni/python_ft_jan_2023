
class Ninja:
    # Class Attribute 
    dojo = "Toky"
    # Constructor
    def __init__(self,name,health ,power,belt, weapons = []):
        # thease attributes are instance attributes
        self.name = name
        self.health = health
        self.power = power
        self.belt = belt
        self.weapons = weapons #default value

    # Methods
    
    # - Instance Methods
    def attack(self,other_ninja):
        other_ninja.health -= self.power/5
        print(f"{self.name} attacked {other_ninja.name} with damage = {self.power/5}")
        return self
    def heal(self):
        self.health += 0.5
    def __repr__(self):
        return f"Name = {self.name} & health = {self.health} 🐱‍👤🐱‍👤"
    @classmethod
    def change_dojo(cls,new_dojo):
        cls.dojo = new_dojo
# - Static Method
    @staticmethod
    def display_stats():
        print(f"Name = {name}")
        print(f"Health = {health}")
        print(f"Power = {power}")
ninja1 = Ninja("Shido", 1,0.9,"black")
ninja2 = Ninja("Kinji", 0.8,0.5,"yellow")
# ninja2.display_stats()
# ninja1.attack(ninja2)
# ninja2.display_stats()
# ninja1.heal()
# ninja1.display_stats()
# print(ninja1)
# print(ninja2.dojo)
ninja3 = Ninja("John", 0.2,0.65, "red")
# print(ninja3.dojo)

class Weapon:
    def __init__(self, data_dict):
        self.power = data_dict["power"]
        self.size = data_dict["size"]
        self.type = data_dict["type"]

Katana = Weapon({"power":10,"size":"big","type":"Sword"})
Daito = Weapon({"power":5,"size":"small","type":"Knife"})

# print(Katana.type, Katana.power)

ninja1.display_stats()

ninja1.weapons.append(Katana)
ninja1.weapons.append(Daito)
for weapon in ninja1.weapons:
    print(weapon.type, weapon.size,weapon.power)

