import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)

color_dict = {0:Fore.CYAN,1:Fore.GREEN,2:Fore.YELLOW,3:Fore.RED,4:Fore.WHITE}

class Brick:

    def __init__(self,x,y,strength,grid,powerup):
        self.x = x
        self.y = y
        self.strength = strength
        self.color = color_dict[strength]
        self.grid = grid
        self.shape = '█'
        self.powerup = powerup

    def draw(self):
        self.grid.set(self.x,self.y,self)

    def remove(self):
        self.grid.unset(self.x,self.y)

    def handle_collision(self):
        if(self.strength != 4):
            self.strength -= 1
            if(self.strength == 0):
                if(self.powerup):
                    self.powerup.enabled = True
                self.remove()
                self.grid.break_brick()
                
            else:
                self.color = color_dict[self.strength]

    def handle_explosion(self):
        neighbours = [(self.x,self.y)]
        while len(neighbours) > 0:
            
            (x,y) = neighbours.pop(0)
            
            self.grid.unset(x,y)
            self.grid.break_brick()
            if(self.grid.isBrick(x,y-1)):
                neighbours.append((x,y-1))

            if(self.grid.isBrick(x,y+1)):
                neighbours.append((x,y+1))

            if(self.grid.isBrick(x+1,y)):
                neighbours.append((x+1,y))

            if(self.grid.isBrick(x-1,y)):
                neighbours.append((x-1,y))

            if(self.grid.isBrick(x-1,y-1)):
                neighbours.append((x-1,y-1))

            if(self.grid.isBrick(x+1,y+1)):
                neighbours.append((x+1,y+1))

            if(self.grid.isBrick(x+1,y-1)):
                neighbours.append((x+1,y-1))

            if(self.grid.isBrick(x-1,y+1)):
                neighbours.append((x-1,y+1))




class Brick1(Brick):
    def __init__(self, x, y,grid,powerup):
        strength = 1
        super().__init__(x, y, strength,grid,powerup)

class Brick2(Brick):
    def __init__(self, x, y,grid,powerup):
        strength = 2
        super().__init__(x, y, strength,grid,powerup)

class Brick3(Brick):
    def __init__(self, x, y,grid,powerup):
        strength = 3
        super().__init__(x, y, strength,grid,powerup)

class Brick4(Brick):
    def __init__(self, x, y,grid,powerup):
        strength = 4
        super().__init__(x, y, strength,grid,powerup)

class ExplodingBrick(Brick):
    def __init__(self, x, y,grid,powerup):
        strength = 0
        super().__init__(x, y, strength,grid,powerup)

class RainbowBrick(Brick):
    def __init__(self, x, y,grid,powerup):
        strength = 1
        self.next_strength = 1
        self.enabled = True
        super().__init__(x, y, strength,grid,powerup)

    def change_color(self):
        if(self.enabled):
        
            self.strength = self.next_strength
            self.next_strength += 1
            if(self.next_strength == 5):
                self.next_strength = 1
            self.color = color_dict[self.strength]
            

        