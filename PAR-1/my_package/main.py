from my_package import car, matrix

matrix = matrix.Matrix()

def level_reader(level):  # Generamos la lista de coches
    cars = []
    levels = open("niveles.txt", "r")
    index = 0
    levels.readline()
    if level != 1:
        for i in range(level):
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
            cars.append(car.Car(chr(97 + index), carinfo[0], int(carinfo[1]), int(carinfo[2]), int(carinfo[3])))
            index += 1
        else:
            break
    levels.close()
    return cars

def set_level(level):  # Creamos el inicio del nivel, su record y colocamos los coches en la matriz
    record = 0
    matrix.clear_matrix()
    with open("records.txt", "r") as f:
        record_list = f.read().split()
    if len(record_list) < level:
        show_record = "\033[1m" + "SIN RECORD" + "\033[m"
    else:
        record = record_list[level - 1]
        show_record = "\033[1m" + record + " MOVIMIENTOS\033[m"
    show_record = "Nivel " + str(level) + " - " + show_record + "\n"
    cars = level_reader(level)
    for i in range(len(cars)):
        matrix.set_car(cars[i].name, cars[i].orientation, cars[i].fixedpos, cars[i].pos, cars[i].lenght, 0)
    return cars, show_record

def game(level, fixed_max_level, max_level):  # El juego en si mismo
    while True:
        state= True
        cars, show_record = set_level(level)  # Se genera el nivel
        number_of_moves = 0
        while state != 2:
            print(show_record)
            matrix.board()
            mov = input("\nNumero de movimientos: \033[1m" + str(number_of_moves) + "\033[m\n\nIntroduzca su jugada: ")
            print()
            for i in range(len(mov)):
                if ord(mov[i].lower()) >= 97 and ord(mov[i].lower()) <= (len(cars) + 96):
                    index = ord(mov[i].lower()) - 97
                    if mov[i] == mov[i].upper():
                        if matrix.set_car(cars[index].name, cars[index].orientation, cars[index].fixedpos, cars[index].pos, cars[index].lenght, -1) == True:
                            cars[index].set_move(-1)
                            number_of_moves += 1
                        else:
                            print("Movimiento " + mov[i] + " imposible por bloqueo\n")
                            break
                    else:
                        state = matrix.set_car(cars[index].name, cars[index].orientation, cars[index].fixedpos, cars[index].pos, cars[index].lenght, 1)
                        if state == True:
                            cars[index].set_move(1)
                            number_of_moves += 1
                        elif state == 2:
                            number_of_moves += 1
                            break
                        else:
                            print("Movimiento " + mov[i] + " imposible por bloqueo\n")
                            break
                else:
                    print("Introduzca un identifucador de movimiento valido\n")
        matrix.board()
        # Desde aqui
        data = ""
        with open("records.txt", "r") as f:
            record_list = f.readline().split()
        if max_level == level:
            record_list.append(str(number_of_moves))
            max_level += 1
            print("\nENHORABUENA, HA COMPLETADO EL NIVEL!\n\nMovimientos: " + str(number_of_moves) + "\n")
        else:
            if int(record_list[level - 1]) > number_of_moves:
                record_list[level - 1] = str(number_of_moves)
                print("\nENHORABUENA, HA COMPLETADO EL NIVEL!\n\nNUEVO RECORD: " + str(number_of_moves) + " movimientos\n")
            else:
                print("\nENHORABUENA, HA COMPLETADO EL NIVEL!\n\nMovimientos: " + str(number_of_moves) + "\n")
        for i in range(len(record_list)):
            data += record_list[i] + " "
        with open("records.txt", "w") as f:
            f.write(data)
            f.truncate()
        # Hasta aqui sobreescribimos el fichero de recorsds
        if level == fixed_max_level:
            print("ENHORABUENA, HA COMPLETADO EL JUEGO!")
            print()
            return False
        else:
            continue_game = input("Desea jugar el siguiente nivel [S/N/M(Menu)]: ").upper()
            if continue_game == "S":
                level += 1
            elif continue_game == "N":
                return False
            elif continue_game == "M":
                return True
            else:
                print("Introduzca un comando valido")

def main():
    game_state = True
    max_length = 0
    level = -1
    # Desde este punto
    with open("niveles.txt", "r") as f:
        fixed_max_level = int(f.readline())
    try:
        open("records.txt", "r")
    except:
        open("records.txt", "x")
    while game_state == True:
        with open("records.txt", "r") as f:
            records = f.read().split()
            max_level = len(records) + 1
        for i in range(len(records)):
            if max_length < len(records[i]):
                max_length = len(records[i])
        print("┌─────────┐\n│ ParKing │\n└─────────┘\n\nElija el nivel:\n")
        for i in range(fixed_max_level):
            if i < len(records):
                    print("Nivel " + str(i + 1) + " " * (len(str(fixed_max_level)) - (len(str(i + 1)) - 1)) + "--> " + " " * (max_length - len(records[i])) + "\033[1;32m" + records[i] + " MOVIMIENTOS" + "\033[m")
            elif i == len(records):
                print("Nivel " + str(i + 1) + " " * (len(str(fixed_max_level)) - (len(str(i + 1)) - 1)) + "--> " + "\033[1;93m" + "DESBLOQUEADO" + "\033[m")
            else:
                print( "Nivel " + str(i + 1) + " " * (len(str(fixed_max_level)) - (len(str(i + 1)) - 1)) + "--> " + "\033[1;31m" + "BLOQUEADO" + "\033[m")
        print ("\033[1;94mIntroduzca 0 para salir\033[m")
        level = int(input("\nNivel seleccionado: "))
        if level == 0:
            return
        elif level <= max_level:
            print()
            game_state = game(level, fixed_max_level, max_level)
            print()
        else:
            print("\nIntroduzca un nivel valido\n")
        # Hasta este, se genera un "menu" q nos muestra los niveles disponibles con sus records

if __name__ == "__main__":
    main()