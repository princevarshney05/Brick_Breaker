import os
import Brick
import colorama
from colorama import Fore,Back,Style
import grid_layout

class Board:

    def __init__(self,name):
        
        self.lives = 3
        self.score = 0
        self.time = 0
        self.level = 1
        self.player_name = name
        self.length = 35
        self.breadth = 70
        self.matrix = [[' ' for i in range(self.breadth)] for j in range(self.length)]
        self.number_of_bricks = 0
        
        self.reset_board()
        
            
        
    def reset_board(self):
        self.matrix = [[' ' for i in range(self.breadth)] for j in range(self.length)]
        for i in range(self.length):
            self.matrix[i][0] = '|'
            self.matrix[i][self.breadth-1] = '|'
        for i in range(self.breadth):
            self.matrix[0][i] = '_'
        


    def set(self,x,y,ch):
        self.matrix[x][y] = ch
    

    def unset(self,x,y):
        self.matrix[x][y] = " "

    def set_time(self,val):
        self.time = round(self.time + val,2)


    def get(self,x,y):
        return self.matrix[x][y]

    def reduce_lives(self):
        self.lives -= 1
        if(self.lives == 0):
            #os.system('clear')
            print("Game Over")
            exit()
        
            
    def isBrick(self,x,y):
        return isinstance(self.matrix[x][y],Brick.Brick)

    def break_brick(self):
        self.number_of_bricks -= 1
        self.score += 100

    def increase_level(self):
        self.level += 1

    def update_rainbow(self):
        for i in range(grid_layout.x,grid_layout.x+grid_layout.l+1):
            for j in range(20,50):
                if(isinstance(self.get(i,j),Brick.RainbowBrick)):
                    self.get(i,j).change_color()

    def reset_time(self):
        self.time = 0
        
        

    def print_board(self):
        str = ''
        str += f'                              Level:{self.level}\n'
        str += f" {self.player_name}           Lives:{self.lives}             Score:{self.score}             Time:{self.time}\n"
        
        for i in range(self.length):
            for j in range(self.breadth):
                if(self.isBrick(i,j)):
                    brick = self.matrix[i][j]
                    form = brick.color + brick.shape + Fore.RESET
                    str += f'{form}'
                else:
                    str += f'{self.matrix[i][j]}'
                
            str += '\n'
        return str


