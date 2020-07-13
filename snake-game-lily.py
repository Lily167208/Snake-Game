#link to trinket project: 
#https://trinket.io/python/e6a39e94df

from processing import *
import random

def setup():
  frameRate(30)
  size(500, 300)
  noStroke()

#changing variables
snake_x = random.randint(10,480)
snake_y = random.randint(10,280)
snake_size = 20

apple_x = random.randint(10,480)
apple_y = random.randint(10,280)
apple_size = 15

apple_color = color(255, 107, 107)

direction = "L"
speed = 5

score = 0

game_over = False

#keyPressed has to go before run()
def keyPressed():
  global direction
  if keyCode == 37:
   direction = "L"
  
  if keyCode == 39:
   direction = "R"
  
  if keyCode == 38:
   direction = "U"
  
  if keyCode == 40:
   direction = "D"

def moveSnake():
  global snake_x, snake_y, speed
  if direction == "R":
    snake_x=snake_x+speed
  if direction == "L":
    snake_x=snake_x-speed
  if direction == "D":
    snake_y=snake_y+speed
  if direction == "U":
    snake_y=snake_y-speed

def snakeEatsApple():
  global apple_x, apple_y, apple_color, speed, score
  if pointInRect(snake_x, snake_y, apple_x, apple_y, apple_size, apple_size) == True or pointInRect(snake_x + snake_size, snake_y, apple_x, apple_y, apple_size, apple_size) == True or pointInRect(snake_x, snake_y + snake_size, apple_x, apple_y, apple_size, apple_size) == True or pointInRect(snake_x + snake_size, snake_y + snake_size, apple_x, apple_y, apple_size, apple_size) == True:
    apple_x = random.randint(10,480)
    apple_y = random.randint(10,280)
    # change apple color
    newRed = random.randint(0, 255)
    newGreen = random.randint(0, 255)
    newBlue = random.randint(0, 255)
    apple_color = color(newRed,newGreen,newBlue)
    # Speed up
    speed = speed+0.5
    # score points
    score = score+1

def lost():
  global game_over
  if snake_x>= 500 or snake_x<= 0:
    game_over = True
  if snake_y>= 300 or snake_y<= 0:
    game_over = True

def draw():
  if game_over == True:
    background(210, 11, 0)
    textSize(70)
    text("Game Over",70,150)
  else:
    background(0, 0, 0)
    #draw apple
    fill(apple_color)
    rect(apple_x, apple_y, apple_size, apple_size)
    #draw snake
    snake_color = color(255, 255, 255)
    fill(snake_color)
    rect(snake_x, snake_y, snake_size, snake_size)
    #move snake
    moveSnake()
    # check if snake eats apple
    snakeEatsApple()
    #lost
    lost()
    #score
    textSize(20)
    text("Score="+str(score), 5, 20)
    #game over


def pointInRect(pt_x, pt_y, rect_x, rect_y, rect_w, rect_h):
  if (pt_x > rect_x) and (pt_x < rect_x + rect_w) and (pt_y > rect_y) and (pt_y < rect_y + rect_h):
    return True
  else:
    return False

run()
