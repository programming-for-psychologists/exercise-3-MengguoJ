import random

LIST = []
for i in range(6):
    list = []
    for j in range(2):
        list.append([i,'masked','right'])
    #    print i,'masked','right'
    #    print i,'masked','left'
        list.append([i,'masked','left'])
    LIST.extend(list)


    for k in range(1):
    #    print i,'nonmasked','right'
        list.append([i,'nonmasked','right'])
    #    print i,'nonmasked','left'
        list.append([i,'nonmasked','left'])
    LIST.extend(list)

random.shuffle(LIST)

for i in range(36):
    print LIST[i]
