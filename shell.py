import core, sys, time, colored
from termcolor import colored, cprint
from colored import stylize, fg
typing_speed = 17  #wpm


def slow_type(t):
    return input(t)
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()


def display_current_information(Gladiator_1, Gladiator_2, choose_name1,
                                choose_name2):
    Gladiator1 = '{}||| Class: {} ||| {} Health ||| {} Rage/Magic'.format(
        choose_name1,
        str(Gladiator_1.getName()), Gladiator_1.health, Gladiator_1.rage)
    Gladiator2 = '{}||| Class: {} ||| {} Health ||| {} Rage/Magic'.format(
        choose_name2,
        str(Gladiator_2.getName()), Gladiator_2.health, Gladiator_2.rage)
    cprint(Gladiator1, 'yellow')
    cprint(Gladiator2, 'green')


def display_menu(attacker):
    if attacker.getName() in [
            'Barbarian', 'Noble', 'Cavalier', 'General', 'Valkyrie',
            'Assassin', 'Dragonmaster'
    ]:
        print_menu = '\nWhat would you like to do?\n-1.Attack:\t\t\t0 Rage Required.\n-2.Apothecary\'s Satchel:\t10 Rage Required.\n-3.Pass:\t\t\t0 Rage Required.\n-4.Pain Pack:\t\t\t20 Rage Required.\n-5.Quit'
        return print_menu
    else:
        print_menu = 'What would you like to do?\n-1.Cast Spell:\t\t\t0 Magic Required.\n-2.Heal:\t\t\t10 Magic Required.\n-3.Pass:\t\t\t0 Magic Required.\n-4.Pain Pack:\t\t\t20 Magic Required.\n-5.Quit'
        return print_menu


def menu(Gladiator_1, Gladiator_2, turn, choose_name, choose_name1,
         choose_name2):
    while True:
        if turn == 0:
            attacker = Gladiator_1
            defender = Gladiator_2
            turn += 1
            name = str(attacker.getName()) + ':'
            choose_name = choose_name1
            name_choose = choose_name2
        elif turn == 1:
            attacker = Gladiator_2
            defender = Gladiator_1
            turn = 0
            name = str(attacker.getName()) + ':'
            choose_name = choose_name2
            name_choose = choose_name1
        attacker.special(defender, choose_name)
        if Gladiator_1.is_dead() == True:
            display_current_information(Gladiator_1, Gladiator_2, choose_name1,
                                        choose_name2)
            quit()
        if Gladiator_2.is_dead() == True:
            display_current_information(Gladiator_1, Gladiator_2, choose_name1,
                                        choose_name2)
            quit()
        display_current_information(Gladiator_1, Gladiator_2, choose_name1,
                                    choose_name2)
        name = choose_name + ' | ' + str(attacker.getName()) + ':'
        gladiator = attacker
        cprint('\n~~~~~~~~~~~~~~~~~~~~~~~~', 'magenta')
        cprint(name, 'magenta')
        cprint('~~~~~~~~~~~~~~~~~~~~~~~~', 'magenta')

        print_menu = display_menu(attacker)
        print(stylize(print_menu, fg("deep_sky_blue_1")))
        menu1 = slow_type(stylize('\n\n\n>>>', fg("yellow_1")))
        if menu1 == '1':
            if attacker.getName() in [
                    'Barbarian', 'Noble', 'Cavalier', 'General', 'Valkyrie',
                    'Assassin', 'Dragonmaster'
            ]:
                print(
                    stylize(
                        attacker.attack(defender, name_choose, choose_name2),
                        fg('royal_blue_1')))
                if Gladiator_1.is_dead() == True:
                    display_current_information(Gladiator_1, Gladiator_2,
                                                choose_name1, choose_name2)
                    quit()
                if Gladiator_2.is_dead() == True:
                    display_current_information(Gladiator_1, Gladiator_2,
                                                choose_name1, choose_name2)
                    quit()
            else:
                cprint(
                    attacker.attack(defender, name_choose, choose_name),
                    'green')
                if Gladiator_1.is_dead() == True:
                    display_current_information(Gladiator_1, Gladiator_2,
                                                choose_name1, choose_name2)
                    quit()
                if Gladiator_2.is_dead() == True:
                    display_current_information(Gladiator_1, Gladiator_2,
                                                choose_name1, choose_name2)
                    quit()
        elif menu1 == '2':
            if attacker.getName() in [
                    'Barbarian', 'Noble', 'Cavalier', 'General', 'Valkyrie',
                    'Assassin', 'Dragonmaster'
            ]:
                cprint(attacker.inventory_heal(), 'yellow')
            else:
                cprint(attacker.heal(choose_name1), 'yellow')
        elif menu1 == '3':
            cprint('\nTurn Passed.\n', 'red', attrs=['bold', 'underline'])
        elif menu1 == '4':
            cprint(
                attacker.inventory_harm(defender),
                'blue',
                attrs=['bold', 'underline'])
            if Gladiator_1.is_dead() == True:
                display_current_information(Gladiator_1, Gladiator_2,
                                            choose_name1, choose_name2)
                quit()
            if Gladiator_2.is_dead() == True:
                display_current_information(Gladiator_1, Gladiator_2,
                                            choose_name1, choose_name2)
                quit()
        elif menu1 == '5':
            cprint('\n' + choose_name1 + ': SURVIVED!\n' + choose_name2 +
                   ': SURVIVED!', 'blue')
            quit()
        else:
            print('\nInvalid input. Try again.\n\n')


def description():
    while True:
        description = input(
            stylize(
                '''\nWhich classes\' description would you like to view?\n\n
        1. Barbarian
        2. Wizard
        3. Bishop
        4. Noble
        5. Cavalier
        6. General
        7. Valkyrie
        8. Assassin
        9. Troubadour
        10. Dragonmaster
        
        M: Return to The Beginning.
        Q. Quit.\n\n-''', fg("plum_3"))).title()

        if description == '1':
            print(
                stylize('''
                1. Barbarian: While not known for their etiquette or intelligence, Barbarians
                are incredibly strong, can take damage well, and fight for those
                who cannot fight for themselves. They tend to favor "Killer Axes" that sometimes, when
                outnumbered or outmatched, allow them to call upon deceased warriors to strengthen the
                silver and sharpen the bit.
                Brash and well-liked, but easily tricked. Gentle Giants.
                
                Name of Special: Warrior's Spirit
                Triggered: When Health is under 30
                Effect: Low Atk is raised 10 points and High Atk is raised 15 points.''',
                        fg("plum_3")))
        elif description == '2':
            print(
                stylize('''
            2. Wizard: Drawing on the subtle weave of magic that permeates the cosmos, 
            wizards cast spells from elements such as explosive fire, arcing lightning and freezing rain.
            Their wands appear in their hands whenvever needed, and draw power from the strength of
            the caster's soul. Old Wizards are revered and respected as high members of society.
            Curious and wise.
            
            Name of Special: Aligned Skies
            Triggered: When Health is under 20
            Effect: Wizard's opponent is hurt by 15 points.''',
                        fg("light_green_2")))

        elif description == '3':
            print(
                stylize('''
            3. Bishop: Men and Women of the cloth who, under divine light, rid the
            Earth of the unholy. Their weapons are their staves, engraved with a special mark at the bottom
            for each individual, with a unique jewel at the top.They are given to them
            when they mature, or when they first truly see the Divine Light. 
            Understanding and gentle. Tend to stay in one place.
            
            Name Of Special: Holy Ground
            Triggered: When health is under 35
            Effect: Bishop is healed 15 points.''', fg("tan")))

        elif description == '4':
            print(
                stylize('''
            4. Noble: An honest hero of high birth and exalted rank. They attack with
            pure weapons of silver and gold, enchanted by Wizards to send the defender's
            souls to a better place. They can call upon their retainer if outmatched, and
            deliver a crushing blow to protect their lord/lady.
            Kind and open-minded.
            
            Name of Special: High Birth
            Triggered: When health is under 25
            Effect: Noble's Health is raised 5 points and the opponent is dealt 10 damage.''',
                        fg("magenta_2b")))

        elif description == '5':
            print(
                stylize('''   
            5. Cavalier: A gallant or chivalrous person, especially one serving as escort 
            to a Noble of high social position; They groom their horses often, and usually
            form a close bond with their equine partner. The strongest cavaliers eventually
            become Paladins and, in turn, can offer their blade to a Noble that they wish
            to keep from harm and will lay down their lives without hesitation.
            Well-Mannered and self sacrificing.
            
            Name of Special: Lucky Habits
            Triggered: When health is under 25
            Effect: Cavalier's Health and rage is raised by 10 each.''',
                        fg("sky_blue_1")))

        elif description == '6':
            print(
                stylize('''
            6. General: Strong and unmoving, Generals command hoards of soldiers and perform
            very well at yelling commands. They are usually dressed in scores of badges and medals.
            They are rumored to move mountains if needed, and can fell a tree with one strike of
            their weapon. Sometimes Generals go on long, lone journeys to find strength again,
            in times of personal hardship, the length of which no one ever knows.
            Natural leaders. Usually are very loud and have laugh lines.
            
            Name of Special: Piercing Blows
            Triggered: When health is under 20
            Effect: General\'s High Atk raised by 10 and the opponent loses 10 health.''',
                        fg("sea_green_1b")))

        elif description == '7':
            print(
                stylize('''
            7. Valkyrie: Strong and wild, their victory cries echo throughout the skies
            and bring hope into the hearts of the innocent and fear into the hearts of the
            unholy. All Valkyrie's gather at Yggdrasil for leisure, and Asgard for times of war.
            The unworthy or fallen members of Valkyrie are sent to Ginnungagap, a primordial void, 
            filled with mists, that exists between Niflheim and Muspelheim. The most worthy join
            a group of maidens who serve the god Odin and are sent by him to the battlefields 
            to choose the slain who were worthy of a place in Valhalla. They treat their winged 
            horses as family and talk to them as if they were human. 
            Merciless and savage, yet beautiful.
            
            Name of Special: Shrieking War Cry
            Triggered: When health is under 30
            Effect: Valkyrie's rage is raised by 10 and opponent is dealt 5 damage''',
                        fg("light_goldenrod_1")))

        elif description == '8':
            print(
                stylize('''
            8. Assassin: Sneaky and swift, Assassin's would rather pick your pocket than
            engage in social contact. They blend into the shadows well, and the silver of their
            swords "Killing Edges" will pierce your skin before you'd even know that they were
            ever there. Suprisingly good with children. Almost emotionless, but have a weakness
            towards kittens.
            
            Name of Special: Swift Kill
            Triggered: When health is under 10
            Effect: Assassin deals the opponent 20 damage.''', fg("red_1")))

        elif description == '9':
            print(
                stylize('''
            9. Troubadour: A horse-mounted magical class that have pure hearts and clear minds.
            Their wistful gestures and warm eyes are often underestimated, and quite
            wrongfully so. Behind their calm facade, burns the fire of an inner warrior wronged
            too many times. With sharp tongues and earth-shattering magic, they are often commended
            for their intelligence and generosity, as well as their battle prowess. Are very compatible
            with Barbarians.
            
            Name of Special: Sick Of It
            Triggered: When health is under 25
            Effect: Troubadour\'s High Atk is raised by 10 and opponent is hurt by 10 points.''',
                        fg("slate_blue_1")))

        elif description == '10':
            print(
                stylize('''
            10. Dragonmaster: The Dragonai tribe have lived in the Himalayas for centuries,
            and rarely leave their mountains often. As an exception, however, Dragonai who
            have bonded well with a particular dragon and show great skill in fighting depart
            from their home and go in search of great legends to fight, only to
            become legends themselves, the Dragonmasters. They usually bond with one of five
            particular dragons:
            Chinese Fireball
            Welsh Green
            Hungarian Horntail
            Swedish Short-Snout
            Japanese Wind-Waker
            
            Name of Special: Searing Spear
            Triggered: When health is under 20
            Effect: Dragonmaster's rage is raised by 5 and deals opponent 15 damage.''',
                        fg("grey_0")))
        elif description == 'M':
            main()
        elif description == 'Q':
            quit()
        else:
            print('\n\nInvalid Input. Try again.\n\n')


def player_select_1():
    cprint(
        '\nWelcome to Valor A turn-based fighting/strategy game!',
        'cyan',
        attrs=['bold'])
    cprint(
        '\nSelect your class, Player 1!',
        'yellow',
        attrs=['bold', 'underline'])
    cprint('''
        1. Barbarian
        2. Wizard
        3. Bishop
        4. Noble
        5. Cavalier
        6. General
        7. Valkyrie
        8. Assassin
        9. Troubadour
        10. Dragonmaster
        ''', 'magenta')
    cprint('Extra Features:\n', 'yellow', attrs=['bold', 'underline'])
    cprint('''
        11. Description of Classes.
        Q. Quit.''', 'magenta')
    choice = input('\n-').title()
    while True:
        if choice == '1':
            p = core.Barbarian(100, 0, 15, 20)
        elif choice == '2':
            p = core.Wizard(100, 10, 10, 25)
        elif choice == '3':
            p = core.Bishop(100, 10, 15, 17)
        elif choice == '4':
            p = core.Noble(100, 5, 15, 18)
        elif choice == '5':
            p = core.Cavalier(100, 0, 15, 19)
        elif choice == '6':
            p = core.General(100, 0, 15, 21)
        elif choice == '7':
            p = core.Valkyrie(100, 5, 18, 20)
        elif choice == '8':
            p = core.Assassin(100, 5, 17, 20)
        elif choice == '9':
            p = core.Troubadour(100, 10, 18, 20)
        elif choice == '10':
            p = core.Dragonmaster(100, 0, 15, 20)
        elif choice == '11':
            p = 0
            print(description())
            quit()
        elif choice == 'Q':
            quit()
        else:
            print('\nInvalid Input.\n')

        return p


def player_select_2():
    cprint(
        '\nSelect your class, Player 1!',
        'yellow',
        attrs=['bold', 'underline'])
    cprint('''
        1. Barbarian
        2. Wizard
        3. Bishop
        4. Noble
        5. Cavalier
        6. General
        7. Valkyrie
        8. Assassin
        9. Troubadour
        10. Dragonmaster
        ''', 'magenta')
    cprint('Extra Features:\n', 'yellow', attrs=['bold', 'underline'])
    cprint('''
        11. Description of Classes.
        Q. Quit.''', 'magenta')
    choice = input('\n-').title()
    while True:
        if choice == '1':
            p = core.Barbarian(100, 0, 15, 20)
            # barbarian.attack(defender)
        elif choice == '2':
            p = core.Wizard(100, 10, 10, 25)
        elif choice == '3':
            p = core.Bishop(100, 10, 15, 17)
        elif choice == '4':
            p = core.Noble(100, 5, 15, 18)
        elif choice == '5':
            p = core.Cavalier(100, 0, 15, 19)
        elif choice == '6':
            p = core.General(100, 0, 15, 21)
        elif choice == '7':
            p = core.Valkyrie(100, 5, 18, 20)
        elif choice == '8':
            p = core.Assassin(100, 5, 17, 20)
        elif choice == '9':
            p = core.Troubadour(100, 10, 18, 20)
        elif choice == '10':
            p = core.Dragonmaster(100, 0, 15, 20)
        elif choice == '11':
            p = 0
            print(description())
            quit()
        elif choice == 'Q':
            quit()
        else:
            print('\nInvalid Input.\n')

        return p


def choose_name_player1():
    return input(
        stylize('\nWhat is your name, Player 1?\n\n-', fg("hot_pink_2")))


def choose_name_player2():
    return input(
        stylize('\nWhat is your name, Player 2?\n\n-', fg("dodger_blue_2")))


def main():
    choose_name1 = choose_name_player1()
    Gladiator_1 = player_select_1()
    choose_name2 = choose_name_player2()
    Gladiator_2 = player_select_2()
    turn = 0
    choose_name = choose_name2
    menu(Gladiator_1, Gladiator_2, turn, choose_name, choose_name1,
         choose_name2)
    display_current_information(choose_name1, choose_name2, Gladiator_1,
                                Gladiator_2)


if __name__ == '__main__':
    main()