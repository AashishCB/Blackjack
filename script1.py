import random
import time


class Deck:

    def __init__(self, st, rk):
        self.suits = st
        self.ranks = rk
        self.values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
                       'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

    def shuffle(self):
        while True:
            s = random.choice(self.suits)
            r = random.choice(self.ranks)
            card = r + ' of ' + s
            if self.card_present_or_not(card):
                break
            else:
                continue
        return card

    def card_present_or_not(self, card):
        if card in dlr.cards or card in plr.cards:
            return False
        else:
            return True


class Dealer:

    def __init__(self):
        self.cards = []
        self.aces = 0

    def add_two_cards(self):
        card_picked1 = d.shuffle()
        card_picked2 = d.shuffle()
        if card_picked1.split()[0] == 'Ace':
            self.aces += 1
        if card_picked2.split()[0] == 'Ace':
            self.aces += 1
        self.cards.extend([card_picked1, card_picked2])
        print('\nComputer\'s card          <card Hidden> + ', self.cards[1], '\n')
        time.sleep(1)

    def __str__(self):
        return " + ".join(self.cards)

    def hit(self):
        card_picked = d.shuffle()
        if card_picked.split()[0] == 'Ace':
            self.aces += 1
        self.cards.append(card_picked)


class Player:

    def __init__(self):
        self.cards = []
        self.aces = 0

    def add_two_cards(self):
        card_picked1 = d.shuffle()
        card_picked2 = d.shuffle()
        if card_picked1.split()[0] == 'Ace':
            self.aces += 1
        if card_picked2.split()[0] == 'Ace':
            self.aces += 1
        self.cards.extend([card_picked1, card_picked2])
        print('\nPlayer\'s hand            ', plr, "\n")
        time.sleep(1)

    def __str__(self):
        return " + ".join(self.cards)

    def hit(self):
        card_picked = d.shuffle()
        if card_picked.split()[0] == 'Ace':
            self.aces += 1
        self.cards.append(card_picked)
        print('\nPlayer\'s hand            ', plr, "\n", "\n")


class Chips:

    def __init__(self):
        self.chips = 100
        self.bet = 0

    def won(self):
        self.chips += self.bet

    def lose(self):
        self.chips -= self.bet

    def __str__(self):
        return self.chips


class Above_or_not:

    def __init__(self):
        self.sumdlr = 0
        self.sumplr = 0

    def sum_check(self):
        for card in dlr.cards:
            self.sumdlr += d.values[card.split()[0]]

        for card in plr.cards:
            self.sumplr += d.values[card.split()[0]]
        a = dlr.aces
        while self.sumdlr > 21 and a > 0:
            self.sumdlr -= 10
            a -= 1
        b = plr.aces
        while self.sumplr > 21 and b > 0:
            self.sumplr -= 10
            b -= 1
        if self.sumdlr > 21:
            print('\nDealer cards:    ', dlr, '    sum=', abvrnt.sumdlr)
            chip.won()
            return 'Dealer BUSTED'
        elif self.sumplr > 21:
            print('\nPlayer cards:  ', plr, '    sum=', abvrnt.sumplr)
            chip.lose()
            return 'Player BUSTED'
        elif self.sumplr == 21:
            print('\nPlayer cards:  ', plr, '    sum=', abvrnt.sumplr)
            #time.sleep(1)
            print('\nDealer cards:    ', dlr, '    sum=', abvrnt.sumdlr)
            chip.won()
            return 'Player WON'
        elif self.sumdlr == 21:
            print('\nPlayer cards:  ', plr, '    sum=', abvrnt.sumplr)
            #time.sleep(1)
            print('\nDealer cards:    ', dlr, '    sum=', abvrnt.sumdlr)
            chip.lose()
            return 'Dealer WON'
        else:
            return 'False'

print('Welcome to BlackJack!\n\n')
time.sleep(1)
print('INSTRUCTIONS:\n\n')
time.sleep(1)
print('1. Get as close to 21 as you can without going over!\n')
time.sleep(1)
print('2. Dealer hits until she reaches 17.\n')
time.sleep(1)
print('3. Aces count as 1 or 11.\n   Jack, Queen and King count as 10.\n')
time.sleep(1)
print('4. You will have 100 chips\n   It will be used to place bet\n   You cannot bet more than you have\n')
time.sleep(1)
print('5. After you don\'t have any more chips left, the game ends\n')
time.sleep(1)

print('\n\n LET\'S START')
print('\n\n')
time.sleep(1)

lets_play = True
chip = Chips()
while lets_play:
    suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
    ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    chip.bet = int(input('\nHow much would you like to bet?'))
    while chip.bet > chip.chips:
        print('\nYou only have ', chip.chips, ' chips to bet')
        chip.bet = int(input('\nYou can\'t bet more than you have \nHow much would you like to bet?'))
    playing = True
    d = Deck(suits, ranks)
    dlr = Dealer()
    plr = Player()
    dlr.add_two_cards()
    plr.add_two_cards()
    while playing:
        al = 1
        abvrnt = Above_or_not()
        sum_check = abvrnt.sum_check()
        if sum_check in ['Dealer BUSTED', 'Player BUSTED', 'Player WON', 'Dealer WON']:
            print(sum_check)
            playing = False
            break

        hit_or_stand = input("\n\nWould you like to hit or stand?\n")

        if hit_or_stand in ['hit', 'Hit', 'HIT']:
            plr.hit()
            continue
        elif hit_or_stand in ['stand', 'Stand', 'STAND']:
            print("\nPlayer Stands,dealer plays\n")
            while abvrnt.sumdlr < 17:
                #time.sleep(1)
                dlr.hit()
                abvrnt = Above_or_not()
                sum_check = abvrnt.sum_check()
                if sum_check in ['Dealer BUSTED', 'Player BUSTED', 'Player WON', 'Dealer WON']:
                    print(sum_check)
                    al = 0
                    break
            if al != 0:
                if abvrnt.sumplr > abvrnt.sumdlr:
                    print('\nPlayer cards:  ', plr, '    sum=', abvrnt.sumplr)
                    #time.sleep(1)
                    print('\nDealer cards:    ', dlr, '    sum=', abvrnt.sumdlr)
                    chip.won()
                    #time.sleep(1)
                    print("\nPlayer Won")
                elif abvrnt.sumplr < abvrnt.sumdlr:
                    print('\nPlayer cards:  ', plr, '    sum=', abvrnt.sumplr)
                    #time.sleep(1)
                    print('\nDealer cards:    ', dlr, '    sum=', abvrnt.sumdlr)
                    chip.lose()
                    #time.sleep(1)
                    print("\nDealer Won")
                else:
                    print('\nPlayer cards:  ', plr, '    sum=', abvrnt.sumplr)
                    #time.sleep(1)
                    print('\nDealer cards:    ', dlr, '    sum=', abvrnt.sumdlr)
                    #time.sleep(1)
                    print("\nGame Draw")
            playing = False
        else:
            continue
    if chip.chips > 0:
        print('\nPlayer has', chip.chips, 'chips remaining\n')
    else:
        print('\nYou have no chips remaining\n ')
        time.sleep(1)
        print('\n!Game Over!\n')
        time.sleep(1)
        print('\nThank you\n')
        break
    time.sleep(1)
    if input("\nWould you like to play again?") in ['Yes', 'Y', 'YES', 'yes', 'y']:
        continue
    else:
        print('\nQuiting the game\n')
        time.sleep(1)
        print("\nThank you!\n")
        break
time.sleep(1)
print("\nbye\n")
