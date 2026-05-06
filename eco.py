# ---------------- ORGANISM ----------------
class Organism:
    def __init__(self, energy, name):
        self.name = name
        self._energy_level = energy

    def energy(self):
        return self._energy_level

    def alive(self):
        return self._energy_level > 0

    def change_energy(self, amount):
        self._energy_level += amount

        if self._energy_level < 0:
            self._energy_level = 0

    def act(self, world):
        pass


# ---------------- PLANT ----------------
class Plant(Organism):

    def act(self, world):
        # Plants gain energy from sunlight
        self.change_energy(1)

        print(f"{self.name} grows. Energy = {self.energy()}")


# ---------------- ANIMAL ----------------
class Animal(Organism):

    def move(self):
        self.change_energy(-3)

    def act(self, world):
        self.move()


# ---------------- HERBIVORE ----------------
class Herbivore(Animal):

    def act(self, world):

        self.move()

        # Eat plants
        for org in world.organisms:

            if isinstance(org, Plant) and org.alive():

                print(f"{self.name} eats {org.name}")

                org.change_energy(-5)

                self.change_energy(+5)

                break

        print(f"{self.name} Energy = {self.energy()}")


# ---------------- CARNIVORE ----------------
class Carnivore(Animal):

    def act(self, world):

        self.move()

        # Eat herbivores
        for org in world.organisms:

            if isinstance(org, Herbivore) and org.alive():

                print(f"{self.name} eats {org.name}")

                org.change_energy(-5)

                self.change_energy(+5)

                break

        print(f"{self.name} Energy = {self.energy()}")


# ---------------- AQUA ANIMAL ----------------
class AquaAnimal(Animal):

    def act(self, world):

        self.move()

        print(f"{self.name} swims in water.")

        print(f"{self.name} Energy = {self.energy()}")


# ---------------- BIRDS ----------------
class Birds(Animal):

    def move(self):

        print(f"{self.name} flies in sky.")

        self.change_energy(-2)

    def act(self, world):

        self.move()

        print(f"{self.name} Energy = {self.energy()}")


# ---------------- WORLD ----------------
class World:

    def __init__(self):
        self.organisms = []

    def add(self, organism):
        self.organisms.append(organism)

    def simulate(self, days):

        for day in range(days):

            print("\n===== DAY", day + 1, "=====")

            for org in self.organisms:

                if org.alive():

                    org.act(self)


# ---------------- OBJECT CREATION ----------------

# Plants
grass = Plant(10, "Grass")
tree = Plant(20, "Tree")

# Herbivores
deer = Herbivore(25, "Deer")
rabbit = Herbivore(15, "Rabbit")

# Carnivores
tiger = Carnivore(30, "Tiger")
fox = Carnivore(40, "Fox")

# Birds
peacock = Birds(50, "Peacock")
parrot = Birds(60, "Parrot")

# Aqua Animals
fish = AquaAnimal(70, "Fish")
shark = AquaAnimal(80, "Shark")


# ---------------- WORLD OBJECT ----------------
world = World()

world.add(grass)
world.add(tree)

world.add(deer)
world.add(rabbit)

world.add(tiger)
world.add(fox)

world.add(peacock)
world.add(parrot)

world.add(fish)
world.add(shark)


# ---------------- SIMULATION ----------------
world.simulate(3)