import Bomb

class UFO:
    def __init__(self,grid,paddle):
        super().__init__()
        self.grid = grid 
        self.x = 2
        self.y = paddle.y


    def draw(self):
        self.grid.set(self.x,self.y,'_')
        self.grid.set(self.x,self.y+1,'_')
        self.grid.set(self.x,self.y+2,'_')
        self.grid.set(self.x,self.y+3,'_')
        self.grid.set(self.x,self.y+4,'_')
        self.grid.set(self.x+1,self.y,'|')
        self.grid.set(self.x+1,self.y+1,'_')
        self.grid.set(self.x+1,self.y+3,'_')
        self.grid.set(self.x+1,self.y+4,'|')
        
        self.grid.set(self.x+2,self.y+2,'╩')

    def move_left(self):
        if self.y > 1:
            self.y -= 1
    
    def move_right(self):
        if(self.y < self.grid.breadth-1-5):
            self.y += 1

    def remove(self):
        for i in range(self.x,self.x+3):
            for j in range(self.y,self.y+5):
                self.grid.unset(i,j)

    def fire(self):
        return Bomb.Bomb(self.x+3,self.y+2,self.grid)

        