class Car:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model


class EletricalCar(Car):
    def __init__(self,Brand,Model,Batary):
        super().__init__(Brand,Model)
        self.Batary=Batary

    def fullDetails(self):
        return f"Brand:{self.Brand},Model:{self.Model},Batary:{self.Batary}"
    
    @staticmethod
    def carDescription():
        return "Car is a amazing transpoter....etc"


c1 = EletricalCar("Tata", "Tiscon","25kWh")
print(c1.carDescription())

