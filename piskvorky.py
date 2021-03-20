oddelovac = '=' * 45

def zdravice() -> None:
#funkce pozdravi uzivatele a seznami ho s pravidly
    oddelovac1 = '-' * 45
    print('Welcome to Tic Tac Toe')
    print(oddelovac)
    text = ('Each player can place one mark (or stone)', 'per turn on the 3x3 grid. The WINNER is',
            'who succeeds in placing three of their','marks in a:', '*horizontal,', '*vertical or',
            '*diagonal row')
    print('{0:^40s}'.format('RULE GAMES:'))
    for radek in range(len(text)):
        print('{0:<40s}'.format(text[radek]))
    print(oddelovac)
    print('{0:^40s}'.format('''Let's start the game'''))
    print(oddelovac1)


def tisk(desk) -> None:
#funkce vytiskne pole
    print('+---+---+---+')
    print('|{0:^3s}|{1:^3s}|{2:^3s}|'.format(desk['1'], desk['2'], desk['3']))
    print('+---+---+---+')
    print('|{0:^3s}|{1:^3s}|{2:^3s}|'.format(desk['4'], desk['5'], desk['6']))
    print('+---+---+---+')
    print('|{0:^3s}|{1:^3s}|{2:^3s}|'.format(desk['7'], desk['8'], desk['9']))
    print('+---+---+---+')
    print(oddelovac)

def test_vstupu(vstup,desk):
#test, jestli je vstup validni a jestli pole neni obsazene

        if vstup.isdigit() and 0 < int(vstup) < 10:
            if desk[vstup] == '  ':
                print(oddelovac)
                return True


            else:
                print('The field is already occupied, try again.')
                return False

        elif not vstup.isdigit():
            print('You must enter a number between 1 and 9')
            return False

        elif vstup.isdigit() and not (0 < int(vstup) < 10):
            print('The number must be between 1 and 9')
            return False



def test_vyhry(desk):
# test vyhry v radcich a sloupcich
    if desk['1'] == 'O' and desk['2'] == 'O' and desk['3'] == 'O':
        return True
    elif desk['4'] == 'O' and desk['5'] == 'O' and desk['6'] == 'O':
        return True
    elif desk['7'] == 'O' and desk['8'] == 'O' and desk['9'] == 'O':
        return True
    elif desk['1'] == 'O' and desk['4'] == 'O' and desk['7'] == 'O':
        return True
    elif desk['2'] == 'O' and desk['5'] == 'O' and desk['8'] == 'O':
        return True
    elif desk['3'] == 'O' and desk['6'] == 'O' and desk['9'] == 'O':
        return True
    elif desk['1'] == 'X' and desk['2'] == 'X' and desk['3'] == 'X':
        return True
    elif desk['4'] == 'X' and desk['5'] == 'X' and desk['6'] == 'X':
        return True
    elif desk['7'] == 'X' and desk['8'] == 'X' and desk['9'] == 'X':
        return True
    elif desk['1'] == 'X' and desk['4'] == 'X' and desk['7'] == 'X':
        return True
    elif desk['2'] == 'X' and desk['5'] == 'X' and desk['8'] == 'X':
        return True
    elif desk['3'] == 'X' and desk['6'] == 'X' and desk['9'] == 'X':
        return True
# test vyhry na diagonale
    elif desk['1'] == 'X' and desk['5'] == 'X' and desk['9'] == 'X':
        return True
    elif desk['3'] == 'X' and desk['5'] == 'X' and desk['7'] == 'X':
        return True

    elif desk['1'] == 'O' and desk['5'] == 'O' and desk['9'] == 'O':
        return True
    elif desk['3'] == 'O' and desk['5'] == 'O' and desk['7'] == 'O':
        return True
    else:
        return False


def main():
    #prazdne hraci pole
    desk = {'1': '  ', '2': '  ', '3': '  ', '4': '  ', '5': '  ', '6': '  ', '7': '  ', '8': '  ', '9': '  '}

    zdravice()
    tisk(desk)
    znak = 'O'
    pocet = 1
    vyhra = False

    while pocet <= 9 and vyhra == False:
        vstup = input(f'Player {znak} | enter your move number: ')

        zadani = test_vstupu(vstup,desk)
        while zadani == False:
        #smycka pro opravu vstupu
            vstup = input(f'Player {znak} | enter your move number: ')
            if test_vstupu(vstup,desk) == True:
                zadani = True

        #tisk znaku do prislusneho pole
        desk[vstup] = znak
        #tisk aktualizovaneho hraciho pole
        tisk(desk)
        #test, jestli nekdo nevyhral
        if pocet >= 5:
            vyhra = test_vyhry(desk)
            if vyhra == True:
                print('Congratulations, the player {} WON'.format(znak))
                print(oddelovac)
        #test na remizu
        if pocet == 9 and not vyhra:
            print('The game ended with a tie')
            print(oddelovac)

        #dalsi kolo
        pocet += 1
        #zmena soupere
        if znak == 'O':
            znak = 'X'
        else:
            znak = 'O'


main()