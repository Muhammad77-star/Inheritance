class vehicle:
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.maxspeed = max_speed
        self.mileage = mileage
class Bus(vehicle):
    pass
School_bus = Bus("School Volvo", 180,12)
print("Vehicle name", School_bus.name, "Speed",School_bus.maxspeed, "maxspeed",School_bus.mileage, "Mileage"  )
