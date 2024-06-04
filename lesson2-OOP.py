

class Animal:
    def __init__(self, name, hunger=0, zoo_name="Hayaton"):
        """Initialize an Animal object."""
        self._name = name
        self._hunger = hunger
        self._zoo_name = zoo_name

    def get_name(self):
        """Return the name of the animal"""
        return self._name

    def is_hungry(self):
        """Check if the animal is hungry."""
        return self._hunger > 0

    def feed(self):
        """Feed the animal"""
        self._hunger -= 1

    def talk(self):
        """Make the animal talk - implemented in subclasses"""
        pass

class Dog(Animal):
    """Initialize a Dog object"""
    def __init__(self,name,hunger=0):
        super().__init__(name,hunger)

    def talk(self):
        super().talk()
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    """Initialize a Cat object"""
    def __init__(self,name,hunger=0):
        super().__init__(name,hunger)

    def talk(self):
        super().talk()
        print("meow")

    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
    """Initialize a Skunk object"""
    def __init__(self,name,hunger=0,stink_count=6):
        super().__init__(name,hunger)
        self._stink_count = stink_count

    def talk(self):
        super().talk()
        print("tsssss")

    def stink(self):
        print("Dear lord!")

class Unicorn(Animal):

    def __init__(self,name,hunger=0):
        """Initialize a Unicorn object"""
        super().__init__(name,hunger)

    def talk(self):
        super().talk()
        print("Good day, darling")

    def sing(self):
        print("i'm not your toy...")

class Dragon(Animal):
    def __init__(self,name,hunger=0,color="Green"):
        """Initialize a Dragon object"""
        super().__init__(name,hunger)
        self._color = color

    def talk(self):
        super().talk()
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

def main():
    """creates objects by table and add them to a list"""
    Brownie = Dog("Brownie",10)
    Zelda = Cat("Zelda",3)
    Stinky = Skunk("Stinky")
    Keith = Unicorn("Keith",7)
    Lizzy = Dragon("Lizzy",1450)
    Doggo = Dog("Doggo",80)
    Kitty = Cat("Kitty", 80)
    Stinky_Jr = Skunk("Stinky Jr.", 80)
    Clair = Unicorn("Clair", 80)
    McFly = Dragon("McFly", 80)
    zoo_lst = [Brownie,Zelda,Stinky,Keith,Lizzy,Doggo,Kitty,Stinky_Jr,Clair,McFly]

    """for each animal in list: if hungry - feed till it isn't 
    , make it talk and activate original ability"""
    for animal in zoo_lst:
        if animal.is_hungry():
            print(type(animal).__name__ + " " + animal.get_name())
            while animal.is_hungry():
                animal.feed()
        animal.talk()
        if type(animal).__name__ == "Dog":
            animal.fetch_stick()
        if type(animal).__name__ == "Cat":
            animal.chase_laser()
        if type(animal).__name__ == "Skunk":
            animal.stink()
        if type(animal).__name__ == "Unicorn":
            animal.sing()
        if type(animal).__name__ == "Dragon":
            animal.breath_fire()
    print(animal._zoo_name)


if __name__ == "__main__":
    main()