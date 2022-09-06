import Brick
import random
import Powerup


x = 5
l = 5

def make_bricks(i,j,grid,powerup):
    strength = random.choice([1,2,3,4,5])
    
    if strength == 1:
        return Brick.Brick1(i,j,grid,powerup)
        grid.number_of_bricks += 1
    if strength == 2:
        return Brick.Brick2(i,j,grid,powerup)
        grid.number_of_bricks += 1
    if strength == 3:
        return Brick.Brick3(i,j,grid,powerup)
        grid.number_of_bricks += 1
    if strength == 4:
        return Brick.Brick4(i,j,grid,powerup)
    if strength == 5:
        return Brick.RainbowBrick(i,j,grid,powerup)


def make_powerups(i,j,grid,paddle):
    m = random.choice([0,1])
    if(m):
        return Powerup.ExpandPaddle('E',i,j,grid,paddle)
    return Powerup.ShrinkPaddle('S',i,j,grid,paddle)


def make_layout(grid,paddle):
    
    
    ans = []
    rainbow_bricks = []

    for i in range(5,11):
        for j in range(20,50):
            if j-15 == i:
                Brick.ExplodingBrick(i,j,grid,None).draw()
                grid.number_of_bricks += 1
            else:
                if(j%3 == 0 and i%2 == 0):
                    m = random.choice([0,1])
                    if(m):
                        powerup_probability = random.randint(1,10)
                        powerup = None
                        if powerup_probability < 3:
                            powerup = make_powerups(i,j,grid,paddle)
                            ans.append(powerup)
                        brick = make_bricks(i,j,grid,powerup)
                        if(isinstance(brick,Brick.RainbowBrick)):
                            rainbow_bricks.append(brick)
                        brick.draw()

    # brick = Brick.RainbowBrick(5,35,grid,None)
    # rainbow_bricks.append(brick)
    # brick.draw()


    

    return ans,rainbow_bricks

def move_layout(grid,paddle):
    global x,l
    flag = True
    for j in range(20,50):
        if(isinstance(grid.get(x+l,j),Brick.Brick)):
            flag = False
    if(flag):
        l -= 1

    if(x+l >= grid.length-2):
        print("game over")
        exit()



    for i in range(x+l,x-1,-1):
        for j in range(20,50):
            

            grid.set(i+1,j,grid.get(i,j))
            grid.unset(i,j)
    x += 1

def remove_layout(grid):
    for i in range(5,11):
        for j in range(20,50):
            grid.unset(i,j)


    
