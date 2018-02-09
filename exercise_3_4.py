
import random


masklist = ['masked']*4 + ['nonmasked']*2
sidelist = ['right']*3 + ['left']*3

for i in range(6):
    random.shuffle(masklist)
#    print masklist
    random.shuffle(sidelist)

    for j in range(6):
        print i,masklist[j],sidelist[j]
