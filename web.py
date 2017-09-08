from flask import Flask, render_template, redirect, request
import core
app = Flask(__name__)

game = core.Game()


@app.route('/')
def root():
    return render_template('root.html')


def player_select(choice):
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
    else:
        p = None
    return p


@app.route('/menu')
def menu():
    choose_name1 = request.args.get('name_1')
    choice = request.args.get('character_1')
    choose_name2 = request.args.get('name_2')
    choice2 = request.args.get('character_2')
    turn = 0
    choose_name = choose_name2
    Gladiator_1 = player_select(choice)
    Gladiator_2 = player_select(choice2)
    attacker = Gladiator_1
    if Gladiator_1 is None or Gladiator_2 is None or choose_name1 is None or choose_name2 is None:
        return redirect('/')
    else:
        game.set_up(Gladiator_1, Gladiator_2, turn, choose_name1, choose_name2)
        return render_template('menu.html', attacker_name=attacker.getName())


@app.route('/turn')
def turn():
    choice = request.args.get('choice')
    if game.turn == 0:
        attacker = game.Gladiator_1
        defender = game.Gladiator_2
        game.turn += 1
        name = str(attacker.getName()) + ':'
        choose_name = game.choose_name1
        name_choose = game.choose_name2
    elif game.turn == 1:
        attacker = game.Gladiator_2
        defender = game.Gladiator_1
        game.turn = 0
        name = str(attacker.getName()) + ':'
        choose_name = game.choose_name2
        name_choose = game.choose_name1
    if choice == '1':
        attacker.attack(defender, choose_name, name_choose)
    elif choice == '2':
        attacker.heal(choose_name)
    elif choice == '4':
        attacker.inventory_harm(defender)
    return render_template('turn.html', attacker_name=attacker)


# display_current_information(choose_name1, choose_name2, Gladiator_1,
#                             Gladiator_2)


def main():
    app.run()


if __name__ == '__main__':
    main()