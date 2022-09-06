import os
from Board import Board 
from Paddle import Paddle
from Ball import Ball 
from input import input_to, Get
import grid_layout
import time
import UFO
falling_brick_activation = {1:0,2:10,3:5}

os.system('clear')
name = input("Enter your name: ")

getch = Get()

if name == '':
    grid = Board('guest')
else:
    grid = Board(name)

game_started = False

start = time.time()

def initialize_game(grid):
    global game_started
    game_started = False
    paddle = Paddle(grid)
    paddle.draw()
    ball = Ball(paddle,grid)
    ball.draw()
    
    powerup,rainbow_bricks = grid_layout.make_layout(grid,paddle)
    obj = {'ball':ball,'paddle':paddle,'powerup':powerup,'rainbow_bricks':rainbow_bricks}
    return obj

obj = initialize_game(grid)


period = 2
current_bombs = []


    



while True:
    #os.system('clear')
    str = grid.print_board()
    #str += f' {ball.x_speed}   {ball.y_speed}'
    
    print(str)

    ch = input_to(getch)

    obj['paddle'].remove()
    obj['ball'].remove()
    if(grid.level == 3):
        ufo.remove()
    for p in obj['powerup']:
        if(p.enabled):
            p.remove()

    for bomb in current_bombs:
        if(bomb.enabled):
            bomb.remove()
    # for b in obj['rainbow_bricks']:
    #     b.change_color()
        
    #     b.draw()
    grid.update_rainbow()
    if game_started:
        game_started = obj['ball'].move()
    if(ch == 'd'):
        obj['paddle'].move_right()
        if not game_started:
            obj['ball'].move_right()
            if(grid.level == 3):
                ufo.move_right()
    if(ch == 'a'):
        obj['paddle'].move_left()
        if not game_started:
            obj['ball'].move_left()
            if(grid.level == 3):
                ufo.move_left()
    if(ch == 'q'):
        break
    if(ch == 'w'):
        game_started = True
    if(ch == 'x'): #new level
        grid.reset_board()
        obj = initialize_game(grid)
        grid.increase_level()
        grid.reset_time()
        if(grid.level == 4):
            print("game over")
            break
        if(grid.level == 3):
            ufo = UFO.UFO(grid,obj['paddle'])
            ufo.draw()


    obj['paddle'].draw()
    obj['ball'].draw()
    if(grid.level == 3):
        ufo.draw()

    for p in obj['powerup']:
        if(p.enabled):
            p.move()

    end = time.time()
    grid.set_time(end - start)



    if(grid.level == 3):
        if(grid.time >= period):
            bomb = ufo.fire()
            current_bombs.append(bomb)

            period += 2

    for bomb in current_bombs:
        if(bomb.enabled):
            bomb.move()
            

        
    
            

    start = end






