#generating a unique random four colour code for Mastermind

from loading_startscreen import *

gen_color_code = [] #list to store the generated colour code

i = 1
while i<=4:
    rand_color = randrange(1,len(colour))
    if rand_color not in gen_color_code:
        gen_color_code.append(rand_color)
        i+=1
    else:
        continue
#print(gen_color_code,'\n\n')


