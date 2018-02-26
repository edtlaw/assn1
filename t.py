#make 50 maps of 101x101 cells, unblocked and blocked

import random




#cell struc

for var in list(range(50)): #0 , 1 , 2 ,... 48, 49

#    file_object  = open(str(var) +'.txt', 'w')



#    for x in range(101):
#        for y in range(101):
#            a= random.randint(1,10)
#            if a<4:         #write to file x + " " + y "\n"
#                file_object.write(str(x) + ' ' + str(y) + '\n')



#    file_object.close()

    fp = open(str(var) + 'end.txt', 'w')
    b =random.randint(0,100)
    c =random.randint(0,100)
    fp.write(str(b) + ' ' + str(c))
    d =random.randint(0,100)
    e =random.randint(0,100)
    fp.write('\n' + str(d) + ' ' + str(e))

    fp.close()
