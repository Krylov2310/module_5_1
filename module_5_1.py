task = 'Домашняя работа по уроку "Атрибуты и методы объекта."'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        for i in range(1, new_floor + 1):
            if new_floor <= self.number_of_floors >= 1:
                print(f'{self.name} с этажа № {self.number_of_floors} может приехать на этаж № {i}')
            else:
                print(f'{self.name} с этажа № {self.number_of_floors}, приехать на этаж № {new_floor} не сможет,'
                      f' так как такого этажа не существует')
                break


# Исходные данные:
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print()
print(thanks)