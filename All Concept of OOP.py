from abc import ABC, abstractmethod

# Abstraction
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

# Inheritance + Encapsulation
class Car(Vehicle):
    def __init__(self, brand):
        self.__brand = brand  # private attribute

    def start_engine(self):
        print(f"{self.__brand} engine started")

    def get_brand(self):
        return self.__brand

# Main program (Polymorphism in action)
def main():
    car1 = Car("Toyota")
    car2 = Car("Honda")

    vehicles = [car1, car2]

    for v in vehicles:   # Polymorphism: same method behaves differently
        v.start_engine()
        print("Brand:", v.get_brand())

# Programiz will look for this entry point
if __name__ == "__main__":
    main()
