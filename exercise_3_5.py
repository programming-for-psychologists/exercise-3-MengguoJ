
import random


masklist = ['masked']*4*2 + ['nonmasked']*2*2
sidelist = ['right']*3*2 + ['left']*3*2

for i in range(6):
    random.shuffle(masklist)
#    print masklist
    random.shuffle(sidelist)

    for j in range(6*2):
        print i,masklist[j],sidelist[j]
