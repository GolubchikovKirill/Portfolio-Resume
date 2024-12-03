import json

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"Машина бренда - {self.brand}, модель '{self.model}', {self.year} года выпуска."
    
    def save_to_file(self, filename):
        car_date = {
            "brand": self.brand,
            "model": self.model,
            "year": self.year
        }
        with open(filename, "w") as f:
            json.dump(car_date, f)
        print(f"Данные о машине сохранены в {filename}.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, "r") as f:
            car_date = json.load(f)
        return Car(car_date["brand"], car_date["model"], car_date["year"])

    
    def update_year(self, new_year):
        if new_year < 1886:
            print("Год выпуска первой машины - 1886, не корректный год выпуска")
        elif new_year > 2024:
            print(f"Год машины не может быть больше текущего года.")     
        else:
            self.year = new_year
            print(f"Год выпуска машины обновлен на {new_year}")
    
    def age(self):
        if self.year > 2024:
            return "Год машины не должен быть свыше 2024 года."
        return 2024 - self.year

# Создаем экземпляр класса   
car = Car("Volvo", "C50", 2005)
print(car.info())

car.update_year(2010)
print(car.info())

car_age = car.age()

if isinstance(car_age, int):
    print(f"Возраст машины - {car_age} лет.")
else:
    print(car_age)

car_save = car.save_to_file("car_date.json")

car_r = car.load_from_file("car_date.json")
print(car_r.info())

