def repetition(letters,numberBeforeSwitch,numRepetitions):
    new_letters = []
    for i in letters:
        new_letters.extend(i * numberBeforeSwitch)

    new_letters = new_letters * numRepetitions
    for ii in new_letters:
        print ii
