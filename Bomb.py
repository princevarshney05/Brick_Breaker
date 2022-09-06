class Bomb:
    def __init__(self,x,y,grid):
        super().__init__()
        self.x = x
        self.y = y
        self.shape = '⦿'
        self.grid = grid
        self.enabled = True

    def move(self):
        temp = self.x + 1
        
        if temp == self.grid.length-1:
            if(self.grid.get(temp,self.y) == '$'):
                self.grid.lives -= 1
                if(self.grid.lives == 0):
                    print("game over")
                    exit()
            self.enabled = False
            self.remove()
        else:
            self.x = temp
            if(self.grid.get(self.x,self.y) == ' '):
                self.draw()

    def draw(self):
        if(self.enabled):
            self.grid.set(self.x,self.y,self.shape)
    
    def remove(self):
        if(self.grid.get(self.x,self.y) == self.shape):
            self.grid.unset(self.x,self.y)