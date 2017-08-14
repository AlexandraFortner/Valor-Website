import random, core, sys, time
"""
On board:
To not go over 100:
gladiator['Key'] = min(100, gladiator['key'] + val)

To not go less than zero:
gladiator['Key'] = max(0, gladiator['key'] + val)
"""
typing_speed = 17  #wpm


def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


def information():
    health = 100
    rage = 0
    damage_low = random.randint(1, 10)
    damage_high = random.randint(11, 16)
    info = core.new_gladiator(health, rage, damage_low, damage_high)
    Gladiator_1 = info
    Gladiator_2 = info
    # print(Gladiator_1, Gladiator_2)
    print('Gladiator 1: {} Health ||| {} Rage'.format(health, rage))
    print('Gladiator 2: {} Health ||| {} Rage'.format(health, rage))


def menu(inform):
    while True:
        menu1 = slow_type(
            '\nWhat would you like to do?\n-1.Attack\n-2.Heal\n-3.Pass\n-4.Quit\n\n>>>'
        )
        if menu1 == '1':
            core.attack(attacker, defender)
        elif menu1 == '2':
            core.heal(gladiator)
        elif menu1 == '3':
            quit()
        elif menu1 == '4':
            print('\nGladiator 1: SURVIVED!\nGladiator 2: SURVIVED!')
            quit()


def main():
    inform = information()
    menu(inform)


if __name__ == '__main__':
    main()