class Player:
    '''The Player'''

    def __init__(self,name,race,backstory,gender):
        self._name = name
        self._race = race
        self.level = 1
        self._gold = 0
        self.hp = 100
        self._backstory = backstory
        self._strength = 50
        self._agility = 50
        self._interlect = 50
        self._gender = gender

    def report(self):
        return{'Name':self._name,'Race':self._race,'Gender':self._gender,'Backstory':self._backstory,'Gold':self._gold,'Level':self.level,'HP':self.hp,'Strength':self._strength,'Agility':self._agility,'Interlect':self._interlect}

    def stats_init(self,gold,strength,agility,interlect):
        self._gold = gold
        self._strength *= strength
        self._agility *= agility
        self._interlect *= interlect
        
def modifers_init(new_player):
    #race modifers
    if new_player._race == 'Human':
        strength_modifer = 1.2
        interlect_modifer = 0.8
        agility_modifer = 1
    elif new_player._race == 'Elf':
        strength_modifer = 0.9
        interlect_modifer = 1.2
        agility_modifer = 1.1
    else:
        strength_modifer = 0.8
        interlect_modifer = 1
        agility_modifer = 1.2
    #backstory modifers
    if new_player._backstory == 'Slave':
        gold_modifer = 0
        strength_modifer += 0.1
        interlect_modifer -= 0.1
        agility_modifer += 0
    elif new_player._backstory == 'Nobleman':
        gold_modifer = 30
        strength_modifer -=0.2
        interlect_modifer += 0.2 
        agility_modifer += 0
    elif new_player._backstory == 'Blacksmith':
        gold_modifer = 20
        strength_modifer += 0.1 
        interlect_modifer += 0 
        agility_modifer -= 0.1 
    else:
        gold_modifer = 10
        strength_modifer -= 0.2
        interlect_modifer += 0.1
        agility_modifer += 0.1
    new_player.stats_init(gold_modifer,strength_modifer,agility_modifer,interlect_modifer)

def backstory_choice():
    print()
    print('1. Slave')
    print('2. Nobleman')
    print('3. Blacksmith')
    print('4. Thief')
    print()
    backstory = int(input('Please enter the backstory of your hero: '))
    if backstory == 1:
        backstory = 'Slave'
    elif backstory == 2:
        backstory = 'Nobleman'
    elif backstory == 3:
        backstory = 'Blacksmith'
    else:
        backstory = 'Thief'
    return backstory

def race_choice():
    print()
    print('1. Human')
    print('2. Elf')
    print('3. Goblin')
    print()
    race = int(input('Please enter the race of your hero: '))
    if race == 1:
        race = 'Human'
    elif race == 2:
        race = 'Elf'
    else:
        race = 'Goblin'
    return race

def gender_choice():
    print()
    print('1. Male')
    print('2. Female')
    print()
    gender = int(input("Please enter your hero's gender: "))
    if gender == 1:
        gender = 'Male'
    else:
        gender = 'Female'
    return gender

def player_init():
    name = str(input("What is your hero's name: "))
    race = race_choice()
    backstory = backstory_choice()
    gender = gender_choice()
    new_player = Player(name,race,backstory,gender)
    modifers_init(new_player)
    return new_player
    

if __name__ == '__main__':
    player = player_init()
    
