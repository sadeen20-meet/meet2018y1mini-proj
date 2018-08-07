# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name: sadeen siaj
Date: tuesday 7th August 2018
"""
import turtle
import random #We'll need this later in the lab

turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for snake1 in range (START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+= (SQUARE_SIZE) 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    stampt= snake.stamp()
    stamp_list.append(stampt)

###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
LEFT = 1
DOWN = 2
RIGHT = 3
direction = UP
UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
   
    print("You pressed the up key!")

#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
#down
def down():
    global direction
    direction=DOWN
    
    print('you pressed the down key!')
#left
def left():
    global direction
    direction=LEFT
   
    print('you pressed the left key!')
#right

def right():
    global direction
    direction=RIGHT
   
    print('youpressed the right key!')


turtle.onkeypress(up, UP_ARROW) # Create listener for up key

#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.onkeypress(left, LEFT_ARROW)

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
        my_pos==(x_pos+ SQUARE_SIZE, y_pos)
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
        my_pos==(x_pos- SQUARE_SIZE, y_pos)

    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE
    elif direction==UP:
        snake.goto(x_pos, y_pos+SQUARE_SIZE)
        print('you moved up !')
        my_pos==(x_pos, y_pos+SQUARE_SIZE)
    elif direction==DOWN:
        snake.goto(x_pos, y_pos-SQUARE_SIZE)
        print('you moved down!')
        my_pos==(x_pos, y_pos-SQUARE_SIZE)
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("you hit the rigt edge! Game over!")
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print("you hit the left edge! Game over!")
        quit()
    elif new_y_pos >= UP_EDGE:

        print("you hit the up edge! Game over!")
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print("you hit thw down edge! Game ove!")
        quit()
        
    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[0]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove ea    ten food stamp
        print('You have eaten the food!')
    
    #HINT: This if statement may be useful for Part 8

    #pop zeroth element in pos_list to get rid of last the last 
    #piece of the tail
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

turtle.register_shape("trash.gif")

food=turtle.clone()
food.shape("trash.gif")
#Location of food
food_pos = [(100,100), (-100,100), (-100,-100),(100,-100)]
food_stamps = []
# Write code that:
#1. moves the food turtle to each food position
#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!
x=0
for this_food_pos in food_pos:
    food.goto(food_pos[x])
    food_stamp = food.stamp()
    food_stamps.append(food.stamp)
    x=x+1
 

