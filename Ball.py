import random
import Brick
import grid_layout

falling_brick_activation = {1:15,2:10,3:5}

class Ball:
    def __init__(self,Paddle,grid):
        self.x = Paddle.x-1
        self.pad_pos = random.randint(0,Paddle.length-1)
        self.y = Paddle.y + self.pad_pos
        self.grid = grid
        self.paddle = Paddle
        self.x_speed = -1
        self.y_speed = 0
        self.ball_shape = '●'
        self.length = grid.length
        self.breadth = grid.breadth

    def move_left(self):
        if(self.y > 1):
            self.y -= 1
    
    def move_right(self):
        if(self.y < self.breadth-1-self.paddle.length):
            self.y += 1

    

    def check_coordinates(self,x,y):
        if(x>=0 and x<self.length and y>=0 and y<self.breadth):
            return True
        else:
            return False

        
        

        



    def move(self):
        
        flag_x = False
        flag_y = False
        next_x = self.x + self.x_speed
        next_y = self.y + self.y_speed

        if(self.check_coordinates(next_x,next_y) and self.grid.isBrick(next_x,next_y)): #handle brick ball collision
            
            if(self.y < next_y or self.y > next_y):
                self.y = next_y - 1
                self.y_speed = -self.y_speed
                flag_y = True

            if(self.y > next_y):
                self.y = next_y + 1
                self.y_speed = -self.y_speed
                flag_y = True
                

            if(self.x < next_x or self.x > next_x):
                self.x_speed = -self.x_speed
                flag_x = True

            brick=self.grid.get(next_x,next_y)
            if(isinstance(brick,Brick.RainbowBrick)):
                if(brick.enabled):
                    brick.enabled = False
                    
            
            if(brick.strength == 0):
                brick.handle_explosion()
            else:
                brick.handle_collision()
            

        if(next_x <= 0):
            self.x = 1
            self.x_speed = - self.x_speed
            flag_x = True
        if(next_y >= self.breadth - 1):
            self.y = self.breadth - 2
            self.y_speed = - self.y_speed
            flag_y =True
        if(next_y <= 0):
            self.y = 1
            self.y_speed = - self.y_speed
            flag_y =True
        if(next_x >= self.length - 1):
            flag_x = True
            paddle_range = range(self.paddle.y,self.paddle.y+self.paddle.length)
            y_point = (((next_y-self.y)//(next_x-self.x))*(self.length-2-self.x))+self.y
            
            if y_point in paddle_range:
                cost = -(self.paddle.length // 2)
                for i in paddle_range:
                    if(i == y_point):
                        temp = self.y_speed + cost
                        if(temp>3):
                            temp = 3
                        if(temp<-3):
                            temp = -3
                        self.y_speed = temp
                        break
                    cost += 1
                self.x_speed = - self.x_speed
                if(self.grid.time >= falling_brick_activation[self.grid.level]):
                    grid_layout.move_layout(self.grid,self.paddle)
            
            
            else:
                self.pad_pos = random.randint(0,self.paddle.length-1)
                self.y = self.paddle.y + self.pad_pos
                self.x_speed = -1
                self.y_speed = 0
                self.grid.reduce_lives()
                return False

        
        
        if(not flag_x):
            self.x = next_x
        if(not flag_y):
            self.y = next_y

        return True

        
    




    

        
    
    def draw(self):
        self.grid.set(self.x,self.y,self.ball_shape)

    def remove(self):
        self.grid.unset(self.x,self.y)

    def reset_game(self):
        self.x = self.paddle.x-1
        self.pad_pos = random.randint(0,self.paddle.length-1)
        self.y = self.paddle.y + self.pad_pos
