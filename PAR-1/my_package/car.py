class Car:
    def __init__(self, name, orientarion, x, y, lenght): #Establece los valores iniciales de cada coche
        self.name = name
        self.orientation = orientarion
        if orientarion == "H":
            self.fixedpos = y
            self.pos = x
        else:
            self.fixedpos = x
            self.pos = y
        self.lenght = lenght

    def set_move(self, i): #Cambia el valor de la posicion del coche en funcion del movimiento ejecutado
        if i == -1:
            self.pos -= 1
        if i == 1:
            self.pos += 1
