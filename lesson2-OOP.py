

class Animal:
    def __init__(self,name,hunger=0,zoo_name="Hayaton"):
        self._name = name
        self._hunger = hunger
        self._zoo_name = zoo_name



    def get_name(self):
        return self._name

    def is_hungry(self):
        return self._hunger > 0

    def feed(self):
        self._hunger -= 1

    def talk(self):
        pass

class Dog(Animal):
    def __init__(self,name,hunger=0):
        super().__init__(name,hunger)

    def talk(self):
        super().talk()
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def __init__(self,name,hunger=0):
        super().__init__(name,hunger)

    def talk(self):
        super().talk()
        print("meow")

    def chase_laser(self):
        print("Meeeeow")

class Skunk(Animal):
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
        super().__init__(name,hunger)

    def talk(self):
        super().talk()
        print("Good day, darling")

    def sing(self):
        print("i'm not your toy...")

class Dragon(Animal):
    def __init__(self,name,hunger=0,color="Green"):
        super().__init__(name,hunger)
        self._color = color

    def talk(self):
        super().talk()
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")

def main():
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