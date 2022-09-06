class Powerup():
    def __init__(self,shape,x,y,grid):
        self.shape = shape
        self.x = x
        self.y = y
        self.enabled = False
        self.grid = grid

    def draw(self):
        if(self.enabled):
            self.grid.set(self.x,self.y,self.shape)

    def remove(self):
        self.grid.unset(self.x,self.y)

    def move(self):
        self.x += 1
        if(self.x >= self.grid.length-2):
            if(self.grid.get(self.x+1,self.y) == '$'):
                self.action()
            
            self.remove()
            self.enabled=False
        else:

            self.draw()

    def action(self):
        pass

    

class ExpandPaddle(Powerup):
    def __init__(self, shape, x, y, grid,paddle):
        super().__init__(shape, x, y, grid)
        self.paddle = paddle

    def action(self):
        if(self.paddle.length < 7):
            self.paddle.length += 2

class ShrinkPaddle(Powerup):
    def __init__(self, shape, x, y, grid,paddle):
        super().__init__(shape, x, y, grid)
        self.paddle = paddle

    def action(self):
        if(self.paddle.length >3):
            self.paddle.remove()
            self.paddle.length -= 2
            self.paddle.draw()
        

    

    



    