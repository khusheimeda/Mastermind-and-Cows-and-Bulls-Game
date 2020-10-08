#mastermind game code

from random_code_generator import *
#since the generation of the random code is not defined inside a function, as soon as the module is imported all the instructions are executed i.e the code is generated

def display_screen(dis_win): #displays the window
    dis_win.setBackground('black')
    label1 = Text(Point(375,50),'THE COLOURS AVAILABLE ARE (no repetitions)')
    label1.setSize(18)
    label1.setTextColor('pink')
    label1.draw(dis_win)

    xcoord = 115; ycoord = 115

    for i in range(1,13): #loop to print the circles for the user to choose from
        cir = Circle(Point(xcoord,ycoord),15)
        cir.setFill(colour[i])
        cir.draw(dis_win)
        xcoord+=50

    
    line = Line(Point(0,150),Point(800,150))
    line.setOutline('white')
    line.draw(dis_win)


dis_point = Point(300,200); point_rect = Point(600,200) #initial coordinates: set by trial-and-error

def print_rect(dis_win,colour, pos1): #function to print rectangles after comparisons of code is done

    pos2 = Point(pos1.x+10,pos1.y+15)
    rect = Rectangle(pos1,pos2)
    rect.setFill(colour)
    rect.draw(dis_win)

def code_check(dis_win,guess,xpos,ypos): #function to compare code entered by the user with initially set code

    game_win = 0
    #the following nested loop compares each colour selected with each colour generated and returns appropriate results
    for i in range(4):
        pos1 = Point(xpos,ypos-15)
        if guess!=gen_color_code:
            
            for j in range(4):
                if guess[i]==gen_color_code[j] and j==i: #i.e if the colour selected is present in the generated code and in the same position entered
                    #print("light green",guess[i])
                    print_rect(dis_win,'light green',pos1)
                    break
                else:
                    if guess[i]==gen_color_code[j] and j!=i: #i.e if the colour selected is present in the generated code but not in the same postion
                        #print("yellow",guess[i],i,j)
                        print_rect(dis_win,'yellow',pos1)
                        break
                    elif guess[i]!=gen_color_code[j]: #i.e if the selected colour is not present in the code at all
                        #print("red")
                        print_rect(dis_win,'red',pos1)
                        #break
            xpos+=50
        else:
            for j in range(4): #i.e all four colours are present in the correct order : game is won
                print_rect(dis_win,'light green',pos1)
            xpos+=50
            game_win = 1
            #break
    return game_win
                

def print_cir(dis_win,i,y): #print circles selected by player

    global dis_point
    dis_point.y = y
    new_cir = Circle(dis_point,15)
    dis_point.x+=50
    new_cir.setFill(colour[i])
    new_cir.draw(dis_win)

def colour_select(dis_win,y,count_code): # selects colour based on mouse click return coordinates

    display_screen(dis_win)
    
    while(1):
        pt = dis_win.getMouse()
        x_min = 100; x_max = 130;
        
        if pt.y >= 100 and pt.y<=130:
            for i in range(1,13):        #checks which circle was clicked by the user using the coordinates of the circle         
                if pt.x>=x_min and pt.x<=x_max:
                    print_cir(dis_win,i,y)
                    count_code[1]=i
                    count_code[0]+=1
                x_min+=50; x_max+=50
            break

    
def colour_click(dis_win):

    y_init = 200
    for i in range(10):
        selected_colours = [] #list that stores the indices of the corresponding colours picked according to the tuple colour defined in loading_startscreen
        count = 0
        dis_point.x = 300
        count_code = [0,0] #this is just for our reference i.e to know the color picked in every turn
        while count_code[0]<4:
            colour_select(dis_win,y_init,count_code)            
            selected_colours.append(count_code[1])
            #print(count_code)            
            timelag()
            
        game_check = code_check(dis_win,selected_colours,point_rect.x,y_init) #performs comparison of the generated and selected code and returns result
        y_init+=50
        
        if game_check == 1: #game is won, yay :)
            label1 = Text(Point(375,y_init+100),'YOU WIN. CONGRATULATIONS')
            label1.setSize(18)
            label1.setTextColor('pink')
            label1.draw(dis_win)
            score = int(100/(i+1)) + 2000 + randrange(500) #sets score on the basis of whether the game was won, the number of tries and luck factor
            break
        
    if game_check==0: #game is over, and the user lost :(
        label1 = Text(Point(375,y_init+100),'GAME OVER. BETTER LUCK NEXT TIME')
        label1.setSize(18)
        label1.setTextColor('pink')
        label1.draw(dis_win)
        score = 10 + 1000 + randrange(500) #sets score based on luck factor
    dis_win.getMouse()
    timelag()
    dis_win.close()
    return score 
        
def mastermind_main(): #calls respective functions that enables user to play the game 
    start()
    dis_win = GraphWin("Main Screen",800,1000)
    return colour_click(dis_win) #this returns score

#mastermind_main()
