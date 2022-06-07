# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, city_population, room_num):
        self.city_popultaion = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_popultaion


# сделать экземпляр класса person и вызвать новые методы.

person = Person(600, 98)

print(person.city_popultaion)
print(person.get_person_room())
