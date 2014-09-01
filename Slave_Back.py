from Player_class import *
from Options_method import *
from Tests_method import *

def slave_01_00(player_class):
    print()
    print('you wake in the small hours of the moring, you go about your tasks, \nyou clean the nights activitys away and prepare the food.')
    print('As you pass by the store cubbored you pick up a broom \npassing though the coradoors you feels an ery pressances')
    print('Carrying on in to the cortyard the cold morning air hits you like a wall, \nyou spend 5 or so minuets speeping the cortyard')
    print('and as your about to leave you feels cold steal on the back of you neck')
    print("A quiet comanding vioce says 'Don't make a sound'")
    choice = option_3('Fight','Run','Complie')
    if choice == 1:
        outcome = strength_test(player,1)
        if outcome == True:
            print('You spin around and smash your broom on the side of the mans head \nthe broom handle')
        else:
            print('you fail')
    elif choice == 2:
        pass
    else:
        pass
    
    


if __name__ == '__main__':
    player = player_init()
    slave_01_00(player)
