import pandas as pd
import math

rav4 = 870000
fseries = 787000
modely = 786000
camry = 675000
crv = 601000
model3 = 596000
silverado = 592000
hilux = 564000
tucson = 564000

class car: 
    def __init__(self, brand, count) -> None:
        self.brand = brand
        self.count = count

corolla = car("Toyota",1120000)
fseries = car("Ford", 787000)
modely = car("Tesla", 786000)
camry = car("Toyota", 675000)
crv = car("Honda", 601000)
model3 = car("Tesla", 596000)
silverado = car("Chervolet", 592000)
hilux = car("Toyota", 564000)
tucson = car("Hyundai", 564000)

topCars = [corolla, fseries, modely, camry, crv, model3, silverado, hilux, tucson]

result = []
for cars in topCars:
    count = math.ceil(cars.count/10000)
    for i in range(count):
        with open('wilkinson-top-car-data.txt', 'a') as f:
            f.write("\""+cars.brand +"\""+ " ,")
