#loading and start screen

from graphics import *
from timelag import *
from random import *

colour = ('black','blue','green','red','orange','yellow','white','pink','light blue','light green','aqua','purple','grey') #the main tuple to which everything is referred to

def loading(): # uses random module and iteration along with a timelag to create the loading screen
    
    screen = GraphWin('Loading Screen',650,600)
    screen.setBackground('black')
    pt = Point(250,295)
    l = list('LOADING')
    xchar = 260;ychar = 250
    
    for i in l: #prints the word 'LOADING; with delay after each character along with rectangles of random colour that change every function call
        clr = randrange(1,len(colour))
        char_coord = Point(xchar,ychar)
        char = Text(char_coord,i)
        char.setTextColor('white')
        xchar+=20
        rect = Rectangle(pt,Point(pt.x + 20,pt.y + 10))
        pt.x+=20
        char.draw(screen)
        rect.setFill(colour[clr])
        rect.draw(screen)
        timelag()
        
    timelag();timelag()
    screen.close()

def start(): #the starting screen for mastermind: uses random module and time delay

    win = GraphWin("Start Screen",650,600)
    win.setBackground('black')
    text = Text(Point(300,150),"WELCOME TO MASTERMIND")
    text.setSize(25)
    text.setTextColor('cyan')
    text.draw(win)
    
    cir_pt = Point(225,200)
    for i in range(4):  #prints four random circles on the graphics window everytime the function is executed
        rand_circle = randrange(1,len(colour))
        cir = Circle(cir_pt,15)
        cir.setFill(colour[rand_circle])
        cir.draw(win)
        timelag()
        cir_pt.x+=50

    point = Point(300,400)  
    start_text = Text(point,'CLICK ANYWHERE TO PROCEED')
    start_text.setTextColor('pink')
    start_text.draw(win)
    if win.getMouse(): #builtin function that returns a Point object i.e, coordinates of the screen where the cursor was clicked 
        win.close()
        loading()


#start()
