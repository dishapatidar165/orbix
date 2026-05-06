
class orgamism:
    def __init__(self,energy):
        self._energy_level = energy

    def energy(self):
        return self._energy_level
    def alive(self):
        return self._energy_level > 0
    def dead(self):
        self._energy_level = 0
    def act(self,world):
                pass


        #________________plant________________
class plant(orgaism):
    def energy(self)
        pass
    def change_energy(self,amount):
            self._energy_level += amount
        if self._energy_level < 0:
                self._energy_level = 0
    def act(self,world):
            self.change_energy(1)   


            pass 
            #__________________animel____________
class animal(orgaism):
    def energy(self):
        pass
    def change_energy(self,amount):
        self._energy_level += amount
            if self._energy_level < 0:
            self._energy_level = 0
    def move(self,world):
            self.change_energy(-3)
                #_________________carnivorus_____________________
class carnivorus(animal):
    def energy(self):
        pass
    def change_energy(self,amount):
            self._energy_level += amount
            if self._energy_level < 0:
                self._energy_level = 0
                
                
                #_________________herbivorus________________
class herbivore(animal):
    def energy(self):
        pass
    def change_energy(self,amount):
        self._energy_level += amount
        if self._energy_level < 0:
            self._energy_level = 0
    def act(self,world):
            self.change_energy(-3)
            #________________aqua animal_________________
class aqua_animal(animal):
    def energy(self):
        pass
    def change_energy(self,amount):
        self._energy_level += amount
        if self._energy_level < 0:
            self._energy_level = 0
        pass
    def act(self,world):
            self.change_energy(-3)
        #_____________________birds____________________
class birds(animal):
    def energy(self):
        pass
    def change_energy(self,amount):
        self._energy_level += amount
        if self._energy_level < 0:
            self._energy_level = 0
            def.change_energy(-3)