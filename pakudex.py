from pakuri import Pakuri

class Pakudex:
    pakuris: list[Pakuri] = []
    capacity = 0
    def __init__ (self, capacity=20):
        self.capacity = capacity
    def get_size(self):
        return len(self.pakuris)
    def get_capacity(self):
        return self.capacity
    def get_array(self):
        return self.pakuris
    def get_species_array(self):
        if (len(self.pakuris) == 0):
            return []
        else:
            species: list[str] = []
            for pakuri in self.pakuris:
                species.append(pakuri.get_species())
            return species
                
    def get_stats(self, species):
        for pakuri in self.pakuris:
            if (pakuri.get_species() == species):
                return [pakuri.get_attack(), pakuri.get_defense(), pakuri.get_speed()]
        return None
    
    def sort_pakuri(self):
        self.pakuris.sort(key=lambda c: c.get_species())
    
    def add_pakuri(self, species):
        if(len(self.pakuris) < self.capacity):
            p = Pakuri(species)
            self.pakuris.append(p)
            return True
        return False
    
    def evolve_species(self, species):
        for p in self.pakuris:
            if (p.get_species() == species):
                p.evolve()
                return True
        return False