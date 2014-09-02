import random

def strength_test(player,difficulty_modifer):
    roll = random.randint(0,100)
    to_beat = player._strength * difficulty_modifer
    if roll >= to_beat:
        outcome = True
    else:
        outcome = False
    if outcome == True:
        print('Passed')
    elif outcome == False:
        print('Failed')
    return outcome

def agility_test(player,difficulty_modifer):
    roll = random.randint(0,100)
    to_beat = player._agility * difficulty_modifer
    if roll >= to_beat:
        outcome = True
    else:
        outcome = False
    if outcome == True:
        print('Passed')
    elif outcome == False:
        print('Failed')
    return outcome

def interlect_test(player,difficulty_modifer):
    roll = random.randint(0,100)
    to_beat = player._interlect * difficulty_modifer
    if roll >= to_beat:
        outcome = True
    else:
        outcome = False
    if outcome == True:
        print('Passed')
    elif outcome == False:
        print('Failed')
    return outcome
