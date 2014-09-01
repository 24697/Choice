def option_2(o1,o2):
    done = False
    print()
    print('1. {0}'.format(o1))
    print('2. {0}'.format(o2))
    print()
    while done == False:
        try:
            choice = int(input('Please enter an option: '))
            if choice == 1 or choice == 2:
                done = True
            else:
                print('Please enter a Valid option')
                print()
        except ValueError:
            print('Please enter a Valid option')
            print()
    return choice

def option_3(o1,o2,o3):
    done = False
    print()
    print('1. {0}'.format(o1))
    print('2. {0}'.format(o2))
    print('3. {0}'.format(o3))
    print()
    while done == False:
        try:
            choice = int(input('Please enter an option: '))
            if choice == 1 or choice == 2 or choice == 3:
                done = True
            else:
                print('Please enter a Valid option')
                print()
        except ValueError:
            print('Please enter a Valid option')
            print()
    return choice

def option_4(o1,o2,o3,o4):
    done = False
    print()
    print('1. {0}'.format(o1))
    print('2. {0}'.format(o2))
    print('3. {0}'.format(o3))
    print('4. {0}'.format(o4))
    print()
    while done == False:
        try:
            choice = int(input('Please enter an option: '))
            if choice == 1 or choice == 2 or choice == 3 or choice == 4:
                done = True
            else:
                print('Please enter a Valid option')
                print()
        except ValueError:
            print('Please enter a Valid option')
            print()
    return choice
