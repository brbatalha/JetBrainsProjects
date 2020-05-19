def status_machine(water, milk, coffee_beans, cups, money):
    print()
    print('The coffee machine has:')
    print(f'{water} of water')
    print(f'{milk} of milk')
    print(f'{coffee_beans} of coffee beans')
    print(f'{cups} of disposable cups')
    print(f'${money} of money')


def check(item):
    resp = True
    if item == 'espresso':
        if water < 250:
            resp = False
            print('Sorry, not enough water!')
        if coffee_beans < 16:
            resp = False
            print('Sorry, not enough coffee beans!')
        if cups < 1:
            resp = False
            print('Sorry, not enough cups!')
    if item == 'latte':
        if water < 350:
            resp = False
            print('Sorry, not enough water!')
        if milk < 75:
            print('Sorry, not enough milk!')
        if coffee_beans < 20:
            resp = False
            print('Sorry, not enough coffee beans!')
        if cups < 1:
            resp = False
            print('Sorry, not enough cups!')
    if item == 'cappuccino':
        if water < 200:
            resp = False
            print('Sorry, not enough water!')
        if milk < 100:
            print('Sorry, not enough milk!')
        if coffee_beans < 12:
            resp = False
            print('Sorry, not enough coffee beans!')
        if cups < 1:
            resp = False
            print('Sorry, not enough cups!')
    return resp


water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550
while True:
    action = str(input('Write action (buy, fill, take, remaining, exit): > ')).strip().lower()
    while True:
        if action == 'buy' or action == 'fill' or action == 'take' or action == 'remaining' or action == 'exit':
            break
        else:
            action = str(input('Write action (buy, fill, take, remaining, exit): > ')).strip().lower()
    if action == 'exit':
        break
    elif action == 'remaining':
        status_machine(water, milk, coffee_beans, cups, money)
        print()
    elif action == 'buy':
        print()
        kind_of_coffee = str(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main '
                                   'menu: > '))
        if kind_of_coffee == 'back':  # retorna para o menu principal
            continue
        if kind_of_coffee.isnumeric():
            kind_of_coffee = int(kind_of_coffee)
            if kind_of_coffee == 1:
                doing = check('espresso')  # inicia a função para verificar se a máquina possui os ingredientes
                if doing:
                    print('I have enough resources, making you a coffee!')
                    water -= 250
                    coffee_beans -= 16
                    cups -= 1
                    money += 4
            elif kind_of_coffee == 2:
                doing = check('latte')  # inicia a função para verificar se a máquina possui os ingredientes
                if doing:
                    print('I have enough resources, making you a coffee!')
                    water -= 350
                    milk -= 75
                    coffee_beans -= 20
                    cups -= 1
                    money += 7
            elif kind_of_coffee == 3:
                doing = check('cappuccino')  # inicia a função para verificar se a máquina possui os ingredientes
                if doing:
                    print('I have enough resources, making you a coffee!')
                    water -= 200
                    milk -= 100
                    coffee_beans -= 12
                    cups -= 1
                    money += 6
            print()
    elif action == 'fill':
        water += int(input('Write how many ml of water do you want to add: > '))
        milk += int(input('Write how many ml of milk do you want to add: > '))
        coffee_beans += int(input('Write how many grams of coffee beans do you want to add: > '))
        cups += int(input('Write how many disposable cups of coffee do you want to add: > '))
        print()
    elif action == 'take':
        print(f'I gave you ${money}')
        money -= money
        print()
