class Paddle:
    def __init__(self,grid):
        self.length = 5
        self.x = grid.length - 1
        self.y = 35
        self.grid = grid

    def move_left(self):
        if(self.y > 1):
            self.y -= 1
    
    def move_right(self):
        if(self.y < 69-self.length):
            self.y += 1

    def draw(self):
        for i in range(self.length):
            self.grid.set(self.x,self.y+i,'$')
        
    def remove(self):
        for i in range(self.length):
            self.grid.unset(self.x,self.y+i)