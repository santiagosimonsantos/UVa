class Car:
    def __init__(self, orientarion, x, y, length): #Establece los valores iniciales de cada coche
        self.orientation = orientarion
        self.x = (x - 1) * 60 + 60
        self.y = (y - 1) * 60 + 60
        self.length = length