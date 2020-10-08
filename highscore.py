#to set highscores : uses file hadndling

from graphics import *

'''
The following lines in this multiline comment were initially used to input data into the file when it was first created. SInce the file akready has this data it's not written in each time the module is imported.
initial = "HIGH SCORES FOR MASTERMIND AND COWS AND BULLS\n"
f1 = open("HighScores.txt",'w+')
f1.write(init)
f1.write('["xyz", 1270, "M"]\n')
f1.write('["abc", 1330, "C&B"]\n')
#print(len('["xyz",1270,"M"]'))
f1.close()'''


def print_hs(l): #function to print the high scores
    
    win = GraphWin("High Scores",800,600)
    win.setBackground('black')
    t1 = "HIGH SCORES"
    text = Text(Point(400,20),t1)
    text.setTextColor('pink')
    text.setSize(20)
    text.draw(win)
    f=open("HighScores.txt") #opens file
    pt = Point(400,50)
    #print(init,end = '')
    l = sorted(f.readlines()[1:],key = lambda a:a[a.index(',')+1:a.index(',',a.index(',')+2)],reverse = True) #this sorts the list of strings read from the file in descending order of the score ([1:] is done to avoid the first line in the file which is "highscores for ..."
    #print(f.readlines())
    #print(l)
    for i in l:
        if i[-1]=='\n': 
            t = Text(pt,i[1:-2]) #to avoid printing the [] and \n in the string
        else:
            t = Text(pt,i[1:-1]) #to avoid printing the []
        t.setTextColor('white')
        t.draw(win)
        pt.y+=20
    win.getMouse()
    win.close()
    #print()
    
    
def highscore(string): #to store the highscore in a file 
      
    f = open("HighScores.txt",'a') #opens file in append mode, assuming file is already created
    f.write(string)
    f.close()
