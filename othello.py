import os
from time import sleep
def clearscreen():
    os.system('CLS')

class Brick:
    def __init__(self):
        self.side=" "
        self.pchangeble=True


class Playfield:
    def __init__(self,height,length):
        self.ask = input("Input player one name: ")
        self.p1_name = self.ask
        self.ask = input("Input player two name: ")
        self.p2_name = self.ask
        self.turn = "p1"
        self.height=height
        self.length=length
        self.board = []
        self.bricks=[]
        for i in range(height):
            self.board.append([0] * length)
            self.bricks.append([0]*length)
        for i in range(height):
            for j in range(length):
                x2=Brick()
                self.board[i][j] = x2.side
                self.bricks[i][j]=x2
        self.change(4, 3, "○")
        self.change(3, 4, "○")
        self.change(3, 3, "•")
        self.change(4, 4, "•")
        self.update()

    def update(self):
        height=self.height
        length=self.length
        self.board.clear()
        for i in range(height):
            self.board.append([0] * length)
        print(self.board)
        for i in range(height):
            for j in range(length):
                self.board[i][j] = self.bricks[i][j].side
        clearscreen()
        self.print()

    def change(self,position_x, position_y,side):
        self.bricks[position_y][position_x].side=side
        print(self.bricks[position_y][position_x].side)
        self.bricks[position_y][position_x].pchangeble = False

    def player_change(self,position_x, position_y,player):
        if player == "p1":
            side = "•"
        else:
            side = "○"

        if self.bricks[position_y][position_x].pchangeble== True:
            list=[]
            self.bricks[position_y][position_x].side=side
            if x == True:
                if self.turn=="p1":
                    self.turn ="p2"
                else:
                    self.turn ="p1"
            self.update()

    def print(self):
        list = ""
        for i in range(self.height):


            if i==0:
                list ="  1 2 3 4 5 6 7 8\n"

            list = list + str(i + 1)
            for j in range(self.length):
                if j ==(0):
                    list=list +"|" + self.bricks[i][j].side + "|"
                else:
                    list=list+self.bricks[i][j].side+"|"

            list=list+"\n"
        print(list)

    def play(self):

        game_on=True
        while game_on==True:
            try:
                ask=input(self.turn+" input coordinates (x and y, seperate with \",\"): ")
                ask=ask.replace(" ","")
                ask=ask.split(",")
                self.position_x=int(ask[0])-1
                self.position_y=int(ask[1])-1
                if self.bricks[self.position_y][self.position_x].pchangeble == False:
                    self.print()
                    print("That is not a valid placement")
                if self.bricks[self.position_y][self.position_x].pchangeble == True:
                    self.player_change(self.position_x, self.position_y, self.turn)
            except:
                clearscreen()
                self.print()
                print("oops, something went wrong...")



x=Playfield(8,8)

x.play()





