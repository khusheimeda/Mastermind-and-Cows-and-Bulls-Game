from graphics import *
from loading_startscreen import loading
import random

def cows_and_bulls():
    loading() 
    score = 100 #Initial score
    win=GraphWin('Cows and Bulls',900,1000)
    #win.setBackground('black')
    b=list()
    i=1
    while i<=4: #this loop creates a unique 4 digit code in which each digit is an element of list b
        c=random.randrange(1,10)
        if c not in b:
            b.append(c)
            i+=1  
    #print(b)

#cows_and_bulls()


    x=300
    y=100
    for i in range(10):
        txt = Text(Point(x,y),'GUESS: ')
        #txt.setTextColor('white')
        txt.draw(win)
        input_box=Entry(Point(x+100,y),4) #allows the user to input their guess 
        input_box.draw(win) 
        win.getMouse()
        guess=input_box.getText()
        cow=0
        bull=0
        for i in range(4): #checks and compares the user's and the generated number and returns appropriate results
            if int(guess[i])==b[i]:
                cow+=1 #i.e the number and the position match correctly
            elif int(guess[i]) in b:
                bull+=1 #i.e the number is present but in a different position
        (Text(Point(x+300,y),cow)).draw(win)
        (Text(Point(x+350,y),'cow')).draw(win)
        (Text(Point(x+400,y),bull)).draw(win)
        (Text(Point(x+450,y),'bull')).draw(win)
        y+=50
        if cow==4: #i.e game is won by the user :)
            (Text(Point(450,950),'CORRECT')).draw(win)
            score = int(100/(i+1)) + 2000 + random.randrange(500) #
            break
    (Text(Point(450,600),'THE CODE IS : '+str(b[0])+str(b[1])+str(b[2])+str(b[3]))).draw(win) #prints the originally generated code
    win.getMouse()
    win.close()
    return score + random.randrange(500) #RETURNS SCORE
#cows_and_bulls()
