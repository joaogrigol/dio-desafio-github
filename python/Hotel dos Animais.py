#importação da biblioteca para forçar o encerramento do programa
import sys

#definição das funções para impressão das listas e do comportamento de cada fase
def imprimirHotel(hotelFase1):
    for linha in hotelFase1:
        print(linha)

def imprimirHotel(hotelFase2):
    for linha in hotelFase2:
        print(linha)

def imprimirHotel(hotelFase3):
    for linha in hotelFase3:
        print(linha)

def imprimirHotel(hotelFase4):
    for linha in hotelFase4:
        print(linha)

def fase1(hotelFase1):
    print('\nBem vindo à Fase 1. Nessa fase você deve alocar o Rato e o Gato nos espaços com _, sem que Rato e Gato fiquem lado a lado,')
    imprimirHotel(hotelFase1)
    posRato = int(input('Digite a posição para alocar o Rato: '))
    posGato = int(input('Digite a posição para alocar o Gato: '))
    if posRato == 6 and posGato == 3:
        print('Você passou de fase!')
        print('\nEsse é o resultado:')
        hotelFase1[0][2] = 'G'
        hotelFase1[1][1] = 'R'
        imprimirHotel(hotelFase1)
        fase2(hotelFase2)
    else:
        print('Você perdeu! Encerrando o jogo...')

def fase2(hotelFase2):
    print('\nBem vindo à Fase 2. Nessa fase você deve alocar o Osso, o Cão e outro Cão nos espaços com _, sem que Cão e Osso fiquem lado a lado.')
    imprimirHotel(hotelFase2)
    posOsso = int(input('Digite a posição para alocar o Osso: '))
    posCao1 = int(input('Digite a posição para alocar o Cão: '))
    posCao2 = int(input('Digite a posição para alocar o segundo Cão: '))
    if posCao1 == 7:
        if posCao2 == 8 and posOsso == 1:
            print('Você passou de fase!')
            print('\nEsse é o resultado:')
            hotelFase2[0][0] = 'O'
            hotelFase2[1][2] = 'C'
            hotelFase2[1][3] = 'C'
            imprimirHotel(hotelFase2)
            fase3(hotelFase3)
    if posCao1 == 8:
        if posCao2 == 7 and posOsso == 1:
            print('Você passou de fase!')
            print('\nEsse é o resultado:')
            hotelFase2[0][0] = 'O'
            hotelFase2[1][2] = 'C'
            hotelFase2[1][3] = 'C'
            imprimirHotel(hotelFase2)
            fase3(hotelFase3)
    else:
        print('Você perdeu! Encerrando o jogo...')

def fase3(hotelFase3):
    print('\nBem vindo à Fase 3. Nessa fase você deve alocar Gato, Rato e Osso nos espaços com _, sem que Rato e Gato fiquem lado a lado,')
    imprimirHotel(hotelFase3)
    posRato = int(input('Digite a posição para alocar o Rato: '))
    posGato = int(input('Digite a posição para alocar o Gato: '))
    posOsso = int(input('Digite a posição para alocar o Osso: '))
    if posRato == 1 and posGato ==7 and posOsso == 5:
        print('Você passou de fase!')
        print('\nEsse é o resultado:')
        hotelFase3[0][0] = 'R'
        hotelFase3[1][0] = 'O'
        hotelFase3[1][2] = 'G'
        imprimirHotel(hotelFase3)
        fase4(hotelFase4)
    else:
        print('Você perdeu! Encerrando o jogo...')

def fase4(hotelFase4):
    print('\nBem vindo à Fase 4. Nessa fase você deve alocar Queijo, Queijo e Osso nos espaços com _, sem que Rato e Queijo fiquem lado a lado.')
    imprimirHotel(hotelFase4)
    posQueijo1 = int(input('Digite a posição para alocar o Queijo: '))
    posQueijo2 = int(input('Digite a posição para alocar o segundo Queijo: '))
    posOsso = int(input('Digite a posição para alocar o Osso: '))
    if posQueijo1 == 1:
        if posQueijo2 == 3 and posOsso == 2:
            print('\nEsse é o resultado:')
            hotelFase4[0][0] = 'Q'
            hotelFase4[0][1] = 'O'
            hotelFase4[0][2] = 'Q'
            imprimirHotel(hotelFase4)
            final()
    if posQueijo1 == 3:
        if posQueijo2 == 1 and posOsso == 2:
            print('\nEsse é o resultado:')
            hotelFase4[0][0] = 'Q'
            hotelFase4[0][1] = 'O'
            hotelFase4[0][2] = 'Q'
            imprimirHotel(hotelFase4)
            final()
    else:
        print('Você perdeu! Encerrando o jogo...')

def final():
        print('\nVocê venceu todas as fases do jogo!!')
        sys.exit()

#atribuição das variáveis de listas e listas de listas
hotelFase1 = [['*','*','_','G'],['R','_','*','*']]
hotelFase2 = [['_','*','*','*'],['*','C','_','_']]
hotelFase3 = [['_','*','*','*'],['_','G','_','*']]
hotelFase4 = [['_','_','_','*'],['*','R','*','*']]

#programa principal
print('Especificando as posições para jogar com o teclado numérico:')
print('[1,2,3,4]')
print('[5,6,7,8]')

fase1(hotelFase1)