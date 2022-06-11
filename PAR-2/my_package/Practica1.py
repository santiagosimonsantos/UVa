import my_package.car as car

def level_reader(level):  # Generamos la lista de coches
    cars = []
    levels = open("niveles.txt", "r")
    index = 0
    levels.readline()
    if level != 0:
        for i in range(level+1):
            while True:
                carinfo = levels.readline()
                if carinfo[0] == "V" or carinfo[0] == "H":
                    pass
                else:
                    number_of_cars = int(carinfo)
                    break
    else:
        number_of_cars = int(levels.readline())
    while True:
        if index < number_of_cars:
            carinfo = levels.readline()
            cars.append(car.Car(carinfo[0], int(carinfo[1]), int(carinfo[2]), int(carinfo[3])))
            index += 1
        else:
            break
    levels.close()
    return cars

def unlocked_levels(): # Generamos la lista de niveles desbloqueados
    try:
        with open("records.txt", "r") as f:
            record_list = f.read().split()
    except:
        open("records.txt", "x")
        record_list = []
    with open("niveles.txt", "r") as f:
        max_level = int(f.readline())
    return record_list, max_level
