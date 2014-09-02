from Player_class import *
from Options_method import *
from Test_method import *

def slave_01_00(player_class):
    print()
    print('you wake in the small hours of the moring, you go about your tasks, \nyou clean the nights activitys away and prepare the food for the new day.')
    print('As you pass by the store cubbored you pick up a broom \npassing though the coradoors you feels an ery pressances')
    print('Carrying on in to the cortyard the cold morning air hits you like a wall, \nyou spend 5 or so minuets speeping the cortyard')
    print('and as your about to leave you feels cold steal on the back of you neck')
    print("A quiet comanding vioce says 'Don't make a sound'...")
    choice_1 = option_3('Fight','Run','Complie')
    if choice_1 == 1:
        #outcome = strength_test(player,1)
        outcome = True
        if outcome == True:
            print('...You spin around and smash your broom on the side of the mans head \nthe broom shaft shatters.\nThe bandit is out cold.')
            print('You start to hear screams and fighting brake out around the mannor...')
            choice_2 = option_2('Flee','Alert Your Master')
            if choice_2 == 1:
                print('...you diside that now is your best chance to ecape from the god for saken\nplace and start a new life. You charge though the mannor uning your \nknowledge of the house to avoide the bandits and ecape form the mannor house.')
            elif choice_2 == 2:
                print('...You need to alert you master and find out whats happend, using the \nslaves passage ways you arive at the masters quarters quickly, as you \naproch the door you hear shouting vocies coming from inside the room...')
                choice_3 =option_2('evees drop on the convisation','burt in to the room')
                
        else:
            print('...You sping around trying to chatch the stanger unawares but he predicts \nyou attack, chaching the broom in one hand and kickes you to the floor.')
            print('You hit your head on the cold stone slabs.')
    elif choice_1 == 2:
        pass
    elif choice_1 == 3:
        pass
    
    


if __name__ == '__main__':
    player = player_init()
    slave_01_00(player)
