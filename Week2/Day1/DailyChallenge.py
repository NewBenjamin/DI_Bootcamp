# Daily Challenge: Old MacDonald's Farm

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type=None, count=1, **kwargs):
        if animal_type:
            if animal_type in self.animals:
                self.animals[animal_type] += count
            else:
                self.animals[animal_type] = count
        for animal, quantity in kwargs.items():
            if animal in self.animals:
                self.animals[animal] += quantity
            else:
                self.animals[animal] = quantity

    def get_info(self):
        result = f"{self.name}'s farm\n\n"
        for animal, count in self.animals.items():
            result += f"{animal} : {count}\n"
        result += "\n    E-I-E-I-0!"
        return result

    def get_animal_types(self):
        return sorted(self.animals.keys())

    def get_short_info(self):
        animal_types = self.get_animal_types()
        animals_with_s = []
        for animal in animal_types:
            if self.animals[animal] > 1:
                animals_with_s.append(animal + "s")
            else:
                animals_with_s.append(animal)
        if len(animals_with_s) == 1:
            animals_str = animals_with_s[0]
        else:
            animals_str = ", ".join(animals_with_s[:-1]) + " and " + animals_with_s[-1]
        return f"{self.name}'s farm has {animals_str}."


# Test
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_short_info())

# Bonus: kwargs
macdonald.add_animal(cow=3, pig=2)
print(macdonald.get_info())