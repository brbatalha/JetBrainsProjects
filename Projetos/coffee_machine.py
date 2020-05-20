class CoffeeMachine:
    running = False

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.dis_cups = 9
        self.money = 550

        if not CoffeeMachine.running:
            self.start()

    def start(self):
        self.running = True
        while self.running:
            action = str(input('Write action (buy, fill, take, remaining, exit): > ')).strip().lower()
            while True:
                if action == 'buy' or action == 'fill' or action == 'take' or action == 'remaining' or action == 'exit':
                    break
                else:
                    action = str(input('Write action (buy, fill, take, remaining, exit): > ')).strip().lower()
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                self.running = False

    def return_to_menu(self):
        self.start()

    def remaining(self):
        print(f'The coffee machine has:'
              f'\n{self.water} of water'
              f'\n{self.milk} of milk'
              f'\n{self.coffee_beans} of coffee beans'
              f'\n{self.dis_cups} of disposable cups'
              f'\n${self.money} of money')

    def buy(self):
        command_buy = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
        if self.dis_cups == 0:
            print('Sorry, not enough disposable cups!')
        else:
            if command_buy == '1':
                if self.water >= 250 and self.coffee_beans >= 16:
                    self.money += 4
                    self.dis_cups -= 1
                    self.water -= 250
                    self.coffee_beans -= 16
                    print('I have enough resources, making you a coffee!')
                elif self.water <= 250:
                    print('Sorry, not enough water!')
                elif self.coffee_beans <= 16:
                    print('Sorry, not enough coffee beans!')
            if command_buy == '2':
                if self.water >= 350 and self.milk >= 75 and self.coffee_beans >= 20:
                    self.money += 7
                    self.dis_cups -= 1
                    self.coffee_beans -= 20
                    self.water -= 350
                    self.milk -= 75
                    print('I have enough resources, making you a coffee!')
                elif self.water <= 350:
                    print('Sorry, not enough water!')
                elif self.milk <= 75:
                    print('Sorry, not enough milk!')
                elif self.coffee_beans <= 20:
                    print('Sorry, not enough coffee beans!')
            if command_buy == '3':
                if self.water >= 200 and self.milk >= 100 and self.coffee_beans >= 12:
                    self.money += 6
                    self.dis_cups -= 1
                    self.water -= 200
                    self.milk -= 100
                    self.coffee_beans -= 12
                    print('I have enough resources, making you a coffee!')
                elif self.water <= 200:
                    print('Sorry, not enough water!')
                elif self.milk <= 100:
                    print('Sorry, not enough milk!')
                elif self.coffee_beans <= 12:
                    print('Sorry, not enough coffee beans!')
            if command_buy == 'back':
                pass

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add: > '))
        self.milk += int(input('Write how many ml of milk do you want to add: > '))
        self.coffee_beans += int(input('Write how many grams of coffee beans do you want to add: > '))
        self.dis_cups += int(input('Write how many disposable cups of coffee do you want to add: > '))

    def take(self):
        print(f'I gave you ${self.money}')
        self.money -= self.money


CoffeeMachine()