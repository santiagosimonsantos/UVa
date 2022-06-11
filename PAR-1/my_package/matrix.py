class Matrix:
    def __init__(self): #Se asignan valores para las "Skins" de los coches al llamar por primera vez a Matrix
        self.start_horizontal = ["┌────", "", "└────"]
        self.mid_horizontal = ["─────", "     ", "─────"]
        self.end_horizontal = ["────┐", "", "────┘"]
        self.start_vertical = ["┌───┐", "", "│   │"]
        self.mid_vertical = ["│   │", "│   │", "│   │"]
        self.end_vertical = ["│   │", "", "└───┘"]

    def clear_matrix(self):  # Establece un tablero vacio
        self.matrix = [
            ["w", "w", "w", "w", "w", "w", "w", "w"],
            ["w", "", "", "", "", "", "", "w"],
            ["w", "", "", "", "", "", "", "w"],
            ["w", "", "", "", "", "", "", "x"],
            ["w", "", "", "", "", "", "", "w"],
            ["w", "", "", "", "", "", "", "w"],
            ["w", "", "", "", "", "", "", "w"],
            ["w", "w", "w", "w", "w", "w", "w", "w"]
        ]

    def set_car(self, name, orientation, fixedpos, pos, lenght, action):  # Tiene 3 funciones, establecer la posicion de los coches al inicio de cada partida, revisar si puede moverse hacia delante o atras y mover el coche en la matriz y comprobar si se ha acabado el juego
        if orientation == "H":
            if action == 0:
                self.matrix[fixedpos][pos] = orientation + name.upper()
                self.matrix[fixedpos][pos + lenght - 1] = orientation + name
                for k in range(lenght - 2):
                    self.matrix[fixedpos][pos + k + 1] = orientation + "-"
                return
            elif action == -1:
                if (self.matrix[fixedpos][pos - 1] == "" or self.matrix[fixedpos][pos - 1] == "x"):
                    self.matrix[fixedpos][pos + lenght - 1] = ""
                    pos -= 1
                else:
                    return False
            else:
                if pos + lenght - 2 == 5 and fixedpos == 3:
                    self.matrix[fixedpos][pos] = ""
                    pos += 1
                    self.matrix[fixedpos][pos] = orientation + name.upper()
                    self.matrix[fixedpos][pos + lenght - 1] = orientation + name
                    for k in range(lenght - 2):
                        self.matrix[fixedpos][pos + k + 1] = orientation + "-"
                    return 2
                elif self.matrix[fixedpos][pos + lenght] == "":
                    self.matrix[fixedpos][pos] = ""
                    pos += 1
                else:
                    return False
            self.matrix[fixedpos][pos] = orientation + name.upper()
            self.matrix[fixedpos][pos + lenght - 1] = orientation + name
            for k in range(lenght - 2):
                self.matrix[fixedpos][pos + k + 1] = orientation + "-"
            return True
        elif orientation == "V":
            if action == 0:
                self.matrix[pos][fixedpos] = orientation + name.upper()
                self.matrix[pos + lenght - 1][fixedpos] = orientation + name
                for k in range(lenght - 2):
                    self.matrix[pos + k + 1][fixedpos] = orientation + "-"
                return
            elif action == -1:
                if self.matrix[pos - 1][fixedpos] == "":
                    self.matrix[pos + lenght - 1][fixedpos] = ""
                    pos -= 1
                else:
                    return False
            else:
                if self.matrix[pos + lenght][fixedpos] == "":
                    self.matrix[pos][fixedpos] = ""
                    pos += 1
                else:
                    return False
            self.matrix[pos][fixedpos] = orientation + name.upper()
            self.matrix[pos + lenght - 1][fixedpos] = orientation + name
            for k in range(lenght - 2):
                self.matrix[pos + k + 1][fixedpos] = orientation + "-"
            return True

    def board(self):  # Dibuja el tablero en una escala 5 char de ancho y 3 char de alto por cada casilla, en función del valor de la casilla
        for i in range(8):
            for j in range(3):
                for k in range(8):
                    if self.matrix[i][k] == "w":
                        print("▒▒▒▒▒", end="")
                    elif self.matrix[i][k] == "":
                        print("     ", end="")
                    elif self.matrix[i][k] == "x":
                        print("\033[1;94m --> \033[m", end="")
                    elif self.matrix[i][k][0] == "H":
                        if i == 3:
                            print("\033[1;94m", end="")
                        if self.matrix[i][k][1] == "-":
                            print(self.mid_horizontal[j], end="")
                        elif self.matrix[i][k][1] == self.matrix[i][k][1].upper():
                            self.start_horizontal[1] = "│" + self.matrix[i][k][1] + "   "
                            print(self.start_horizontal[j], end="")
                        else:
                            self.end_horizontal[1] = "   " + self.matrix[i][k][1] + "│"
                            print(self.end_horizontal[j], end="")
                        print("\033[m", end="")
                    elif self.matrix[i][k][0] == "V":
                        if self.matrix[i][k][1] == "-":
                            print(self.mid_vertical[j], end="")
                        elif self.matrix[i][k][1] == self.matrix[i][k][1].upper():
                            self.start_vertical[1] = "│ " + self.matrix[i][k][1] + " │"
                            print(self.start_vertical[j], end="")
                        else:
                            self.end_vertical[1] = "│ " + self.matrix[i][k][1] + " │"
                            print(self.end_vertical[j], end="")
                print()
