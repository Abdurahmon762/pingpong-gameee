# Simple Pong game in Python 3 using Tkinter module J Joubert 22 Oct 2019
# Created on mac - using os for sounds
# winsound for windows
# Game speed may have to be adjusted for windows

# Use # to remove sound when scoring or for import os

from tkinter import *
import os # Optional for sounds in mac osX

# import time # and time.sleep(0.017) windows?


win = Tk() # Create window (tkinter.Tk)
win.title("Pong Game Python 3 Tkinter")
win.resizable(0, 0) # Can be left out - cannot resize window
canvas = Canvas(win, width=800, height=600,bg='black') # tkinter.Canvas is placed in window(win) 800 pixelsx600pixels, black background
canvas.pack() # Pack the canvas in win to show the canvas

p1score = 0 # Set scores to 0
p2score = 0


# Coordinates gives (top left x,y, bottom right x,y) or simply the (left x, top y, right x, bottom y)

p1=canvas.create_rectangle(40, 255, 60, 345, fill='white')  # Create paddle 1 between 40-60 in x and 255-345 in y and make it white

p2=canvas.create_rectangle(740, 255, 760, 345, fill='white') # Create paddle 2 (740-760 x and 255-345 y)

ball = canvas.create_oval(400,300,420,320, fill='white') # Create ball (400-420 in x and 300-320 in y therefor 20x20pixels)

score = canvas.create_text(380,50, fill = 'red', font="Courier 24 normal",
                           text=(f"Player 1: {p1score}   Player 2: {p2score}"))


# for paddle 1
def move_p1(event):
    if event.keysym == "w" and p1y0 > 0: # Move p1 up if top part paddle 1 y0 is not at the top of the window
        canvas.move(p1, 0, -30) # Move p1 x0 and y-30 (not left/right only up with y getting smaller)
        
    elif event.keysym == "s" and p1y1 < 600: # move p1 down if bottom part y1 is not at bottom of window
        canvas.move(p1, 0, 30)


# for paddle 2
def move_p2(event):
    if event.keysym == "Up" and p2y0 > 0:
        canvas.move(p2, 0, -30)
    elif event.keysym == "Down" and p2y1 < 600:
        canvas.move(p2, 0, 30)
    

# Assign keys
canvas.bind_all("<KeyPress-w>", move_p1)
canvas.bind_all("<KeyPress-s>", move_p1)
canvas.bind_all("<KeyPress-Up>", move_p2)
canvas.bind_all("<KeyPress-Down>", move_p2)


# Asign values to give the speed to the ball - can change these
# May have to change the value in windows due to speed eg 0.05 etc??
x, y = 4, 4

while True:
    
    # move (ball, 9 pixels in x, 9 pixels in y) every time this loop runs
    canvas.move(ball, x, y)

    # coords returns 4 values [x0, y0, x1, y1] as list (top left x and y and bottom right x and y)
    x0, y0, x1, y1 = canvas.coords(ball)    
    # you can also say ball_pos = canvas.coords(ball) - to create a list with ball_pos[0] = x0, ball_pos[2] = x1, etc
    
    p1x0, p1y0, p1x1, p1y1 = canvas.coords(p1)
    p2x0, p2y0, p2x1, p2y1 = canvas.coords(p2)
    
    # Score player 2 (ball passed out on the left side)
    if x0 <=0:
        x *= -1 # x = x* -1  (x becomes positive if negative and negative if positive to change direction left and right
        os.system('say "score"') # This is for mac only
        # To play sound file:
        # os.system('afplay bounce.wav&') e.g. to play wav file in the same directory
        # & is optional to allow game play while the file is playing (otherwise game freezes until sound is finished)
        # Winsound for windows
        
        canvas.coords(ball,400,300,420,320) # move the ball back to middle 400-420 in x and 300-320 in y (top left x,y, bottom right x,y)
        p2score +=1
        canvas.delete(score) # don't overwrite the score - delete and write new score
        score = canvas.create_text(380,50, fill = 'red', font="Courier 24 normal",
                           text=(f"Player 1: {p1score}   Player 2: {p2score}"))
        

    # Score player 2 (ball passed right side)
    if x1>=800:
        x *=-1
        os.system('say "score"')
        canvas.coords(ball,400,300,420,320)
        p1score +=1
        canvas.delete(score)
        score = canvas.create_text(380,50, fill = 'red', font="Courier 24 normal",
                           text=(f"Player 1: {p1score}   Player 2: {p2score}"))
        
    # Bouncing off top or bottom   
    if y0<=0 or y1 >=600:
        # if ball reaches top y0 (top of ball) = 0 (top of screen) or bottom y1 (bottom of ball) = 600 (bottom of screen)
        # y = y * -1 to change direction in y (9 becomes -9 and -9 becomes 9)
        y *= -1
        

    # Bounce paddle:
    
    # Paddle 2
    # x1 = ball left must be more than paddle 2 right = (740 or p2y0) but less than about the middle 755 (must not be past the paddle already)
    # y1 = ball bottom must be lower than the top of the paddle 2 or p2y0
    # y0 = ball top must not be lower than bottom of paddle 2 or p2y1
    
    if x1 >=740 and x1<= 760 and x>0: # paddle2 within 740 to 760 on x axis 
        if y1 >= p2y0 and y0 <= p2y1:
            x *= -1
            
    # Paddle 1
    if x0 >=40 and x0<= 60 and x<0:
        if y1 >=p1y0 and y0 <= p1y1:
            x *= -1
   
    win.update() # update graphics/position of the paddle/ball/score on the screen
    #time.sleep(0.017) # windows?





    

