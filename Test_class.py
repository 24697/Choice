import random

def strength_test(player,difficulty_modifer):
    roll = random.randint(0,100)
    print(roll)
    to_beat = player._strength * difficulty_modifer
    print(to_beat)
    if roll >= to_beat:
        outcome = True
    else:
        outcome = False
    print(outcome)
    return outcome

def agility_test(player,difficulty_modifer):
    roll = random.randint(0,100)
    print(roll)
    to_beat = player._agility * difficulty_modifer
    print(to_beat)
    if roll >= to_beat:
        outcome = True
    else:
        outcome = False
    print(outcome)
    return outcome

def interlect_test(player,difficulty_modifer):
    roll = random.randint(0,100)
    print(roll)
    to_beat = player._interlect * difficulty_modifer
    print(to_beat)
    if roll >= to_beat:
        outcome = True
    else:
        outcome = False
    print(outcome)
    return outcome
