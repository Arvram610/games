import os


def clearscreen():
    os.system('CLS')


class Brick:
    def __init__(self):
        self.side = " "
        self.pchangeble = True


class Playfield:
    def __init__(self, height, length):
        self.game_on = True
        self.ask = input("Input player one name: ")
        self.p1_name = self.ask
        self.ask = input("Input player two name: ")
        self.p2_name = self.ask
        self.turn = "p1"
        self.height = height
        self.length = length
        self.board = []
        self.bricks = []
        for i in range(height):
            self.board.append([0] * length)
            self.bricks.append([0] * length)
        for i in range(height):
            for j in range(length):
                x2 = Brick()
                self.board[i][j] = x2.side
                self.bricks[i][j] = x2
        self.change(4, 3, "○")
        self.change(3, 4, "○")
        self.change(3, 3, "•")
        self.change(4, 4, "•")
        self.update()

    def update(self):
        height = self.height
        length = self.length
        self.board.clear()
        for i in range(height):
            self.board.append([0] * length)
        for i in range(height):
            for j in range(length):
                self.board[i][j] = self.bricks[i][j].side
        clearscreen()
        self.print()

    def change(self, position_x, position_y, side):
        self.bricks[position_y][position_x].side = side

        self.bricks[position_y][position_x].pchangeble = False

    def player_change(self, position_x, position_y, player):
        if player == "p1":
            side = "•"
            not_side = "○"

        else:
            side = "○"
            not_side = "•"

        if self.bricks[position_y][position_x].pchangeble:
            list = []
            preliminary_list = []
            x = False
            y_positive = 8 - position_y
            x_positive = 8 - position_x
            x_negative = position_x -1
            y_negative = position_y -1

            if self.bricks[y_negative][x_negative].side == not_side:  # diagonal -x -y
                if y_negative > x_positive:
                    y = x_negative + 1

                else:
                    y = y_negative + 1

                for i in range(y):
                    if self.bricks[position_y - (i + 1)][position_x - (i + 1)].side == not_side:
                        preliminary_list.append(self.bricks[position_y - (i + 1)][position_x - (i + 1)])

                    elif self.bricks[position_y - (i + 1)][position_x - (i + 1)].side == side and not position_x - (
                            i + 1) == position_x - 1 and not position_y - (i + 1) == position_y - 1:
                        for j in preliminary_list:
                            print(j)
                            list.append(j)
                        preliminary_list = []
                        x = True
                        break

                    else:
                        preliminary_list = []
                        break

            if self.bricks[position_y][x_negative].side == not_side:  # negative x
                for i in range(x_negative):
                    if self.bricks[position_y][x_negative - i].side == not_side:

                        preliminary_list.append(self.bricks[position_y][position_x - (i + 1)])

                    elif self.bricks[position_y][x_negative - i].side == side and not position_x - i == position_x - 0:
                        for j in preliminary_list:
                            list.append(j)
                            x = True

                        preliminary_list = []
                        break

                    else:
                        preliminary_list = []
                        break
            print(position_y + 1)
            if self.bricks[y_negative][position_x].side == not_side:  # negative y

                for i in range(position_y+1):
                    if self.bricks[y_negative-i][position_x].side == not_side:
                        preliminary_list.append(self.bricks[position_y - (i + 1)][position_x])

                    elif self.bricks[y_negative-i][position_x].side == side and not position_y-i == position_y-0:
                        for j in preliminary_list:
                            list.append(j)
                            x = True

                        preliminary_list = []
                        break

                    else:
                        preliminary_list = []
                        break
            try:
                if self.bricks[y_negative][position_x+1].side == not_side:  # diagonal +x -y
                    if y_negative+1 > x_positive-1:
                        y = y_negative

                    else:
                        y = x_positive

                    for i in range(y):
                        if self.bricks[position_y - i-1][position_x + i + 1].side == not_side:
                            preliminary_list.append(self.bricks[position_y - i-1][position_x + i + 1])

                        elif self.bricks[position_y - i-1][position_x + i + 1].side == side and not position_x + (
                                i + 1) == position_x + 1 and not position_y + (i + 1) == position_y + 1:
                            for j in preliminary_list:
                                list.append(j)

                            preliminary_list = []
                            x = True
                            break

                        else:
                            print("hello3")
                            preliminary_list = []
                            break
            except:
                pass

            try:
                if self.bricks[position_y][position_x+1].side == not_side:  # positive x

                    for i in range(x_positive):
                        if self.bricks[position_y][position_x + i+1].side == not_side:

                            preliminary_list.append(self.bricks[position_y][position_x + i+1])

                        elif self.bricks[position_y][position_x + i+1].side == side and not position_x - i == position_x - 0:
                            for j in preliminary_list:
                                list.append(j)
                                x = True

                            preliminary_list = []
                            break

                        else:
                            preliminary_list = []
                            break

            except:
                pass

            try:
                if self.bricks[position_y+1][position_x].side == not_side:  # positive y

                    for i in range(y_positive):
                        if self.bricks[position_y+1+i][position_x].side == not_side:
                            preliminary_list.append(self.bricks[position_y + (i + 1)][position_x])

                        elif self.bricks[position_y+1+i][position_x].side == side and not position_y-i == position_y-0:
                            for j in preliminary_list:
                                list.append(j)
                                x = True

                            preliminary_list = []
                            break

                        else:
                            preliminary_list = []
                            break

            except:
                pass

            try:
                if self.bricks[position_y+1][x_negative].side == not_side:  # diagonal -x +y
                    if position_y+1 > x_positive:
                        y = x_negative + 1

                    else:
                        y = position_y+1 + 1

                    for i in range(y):
                        if self.bricks[position_y+1+i][position_x - (i + 1)].side == not_side:
                            preliminary_list.append(self.bricks[position_y+(i + 1)][position_x - (i + 1)])

                        elif self.bricks[position_y+(i + 1)][position_x - (i + 1)].side == side and not position_x - (
                                i + 1) == position_x - 1 and not position_y+(i + 1) == position_y + 1:
                            for j in preliminary_list:
                                print(j)
                                list.append(j)
                            preliminary_list = []
                            x = True
                            break

                        else:
                            preliminary_list = []
                            break
            except:
                pass

            try:
                if self.bricks[position_y+1][position_y+1].side == not_side:  # diagonal -x +y
                    if position_y+1 > x_positive:
                        y = position_y + 1+1

                    else:
                        y = position_y+1 + 1

                    for i in range(y):
                        if self.bricks[position_y+1+i][position_x + (i + 1)].side == not_side:
                            preliminary_list.append(self.bricks[position_y+(i + 1)][position_x + (i + 1)])

                        elif self.bricks[position_y+(i + 1)][position_x + (i + 1)].side == side and not position_x + (
                                i + 1) == position_x + 1 and not position_y+(i + 1) == position_y + 1:
                            for j in preliminary_list:
                                print(j)
                                list.append(j)
                            preliminary_list = []
                            x = True
                            break

                        else:
                            preliminary_list = []
                            break
            except:
                pass

            if x:  # byt spelares tur
                list.append(self.bricks[position_y][position_x])
                if self.turn == "p1":
                    self.turn = "p2"

                else:
                    self.turn = "p1"
            else:
                print("That's not a valid move.")

            for i in list:
                i.side = side
                i.pchangeble = False

            self.update()

    def print(self):
        list = ""
        for i in range(self.height):

            if i == 0:
                list = "  1 2 3 4 5 6 7 8\n"

            list = list + str(i + 1)
            for j in range(self.length):
                if j == (0):
                    list = list + "|" + self.bricks[i][j].side + "|"
                else:
                    list = list + self.bricks[i][j].side + "|"

            list = list + "\n"
        print(list)

    def play(self):


        while self.game_on:
            #try:
                ask = input(self.turn + " input coordinates (x and y, seperate with \",\"): ")
                if ask == "DeBuG":
                    ask = input(self.turn + "input coordinates (x and y, seperate with \",\" )debug: ")
                    ask = ask.replace(" ", "")
                    ask = ask.split(",")
                    position_x = int(ask[0]) - 1

                    position_y = int(ask[1]) - 1
                    color = input("color?")
                    if color == "w":
                        color = "•"
                    else:
                        color = "○"
                    self.change(position_x, position_y, color)
                else:
                    ask = ask.replace(" ", "")
                    ask = ask.split(",")

                    self.position_x = int(ask[0]) - 1

                    self.position_y = int(ask[1]) - 1

                    if self.bricks[self.position_y][self.position_x].pchangeble == False:
                        clearscreen()
                        self.print()
                        print("That's not a valid move.")

                    if self.bricks[self.position_y][self.position_x].pchangeble == True:
                        self.player_change(self.position_x, self.position_y, self.turn)
           # except:
              #  clearscreen()
              #  self.print()
             #   print("oops, something went wrong...")


x = Playfield(8, 8)

x.play()
