class Car:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def show(self):
        print(f"this is my {self.name} and this is my brand {self.brand}")
car1=Car(alto,maruti)
print(car1.name())
print(car1.show())



