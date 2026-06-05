# create a class
class Vehicle:

    # create init method
    def __init__(self, max_speed, mileage):

        # blind the arguements
        self.max_speed = max_speed
        self.mileage = mileage

# Object creation
modelX = Vehicle(240, 18)

# access the variables inside init method
print("Model Max Speed:",modelX.max_speed)
print("Model Mileague:", modelX.mileage)