#Felipe Menino
#Versão 0.9.4.2_FinalRelease
#Importo bibliotecas de request e random
import urllib.request
import random

# Variaveis globais utilizadas
palavra = ''
troca = ''
lista = ''

#Função criada para realizar a escolha da palavra
def escolhe():
    global lista,palavra
    palavra = ''
    if len(lista) == 0:
        #Puxando as palavras do site com requests
        web = urllib.request.urlopen('https://www.ime.usp.br/~pf/dicios/br')
        palavras = web.read()
        web.close()

        #Lista é onde está salvo a lista de palavras extraidas do site
        lista = palavras.decode(encoding='iso8859').lower()
        lista = lista.split()
        palavra = lista[random.randint(0,len(lista))]
    else:
        while len(str(lista[random.randint(0,len(lista))])) > 5:
            palavra = lista[random.randint(0,len(lista))]
    return palavra

def desenha(erradas):
    boneco = ['''
            +----------+
                       |
                       |
                       |
                       |
                       |
                       |
                       |
   =====================''','''
           +----------+
           O          |
                      |
                      |
                      |
                      |
                      |
                      |
   ====================''',
    '''
            +----------+
            O          |
            I          |
                       |
                       |
                       |
                       |
                       |
    =====================''',
    '''
            +----------+
            O          |
           /I          |
                       |
                       |
                       |
                       |
                       |
    =====================''',
    '''
            +----------+
            O          |
           /I\         |
                       |
                       |
                       |
                       |
                       |
    =====================''',
    '''
            +----------+
            O          |
           /I\         |
            I          |
                       |
                       |
                       |
                       |
    =====================''',
    '''
            +----------+
            O          |
           /I\         |
           /I          |
                       |
                       |
                       |
                       |
    =====================''',
    '''
            +----------+
            O          |
           /I\         |
           /I\         |
                       |
                       |
                       |
                       |
    =====================''','''
    ########  ######## ########  ########  ######## ##     ##
    ##     ## ##       ##     ## ##     ## ##       ##     ##
    ##     ## ##       ##     ## ##     ## ##       ##     ##
    ########  ######   ########  ##     ## ######   ##     ##
    ##        ##       ##   ##   ##     ## ##       ##     ##
    ##        ##       ##    ##  ##     ## ##       ##     ##
    ##        ######## ##     ## ########  ########  ####### ''']
    print(boneco[len(erradas)])

#Verifica se o usuário deseja jogar novamente

def jogar_novamente(resposta):
    while 1:
        if resposta.lower() == 'sim':
            forca()
        elif resposta.lower() == 'nao' or resposta.lower() == 'não':
            print("Obrigado por jogar =D")
            exit()
        else:
            print("Caractere invalido")
            resposta = input("Você deseja jogar novamente ? ")
            continue

#Faz a troca da palavra pelo caractere especial
def embaralha(palavra):
    global troca
    troca = ''
    for i in range(0,len(palavra)):
        troca += '_'
    return troca

#Iniciando a estrutura do jogo

def forca():
    global troca,palavra
    contador = 0
    certas = ''
    erradas = ''
    palavra = ''
    escolhe()
    embaralha(palavra)
    desenha(erradas)
    print('\n' + troca)
    #Inicia o loop para verificar o chute do usuário
    while 1:
        if contador == 8:
            print("Suas chances acabaram!!!")
            break
        if troca == palavra:
            erradas = ''
            print("Você ganhou =D")
            jogar_novamente(resposta=input("Você deseja jogar novamente ? \n"))

        print("\nVocê tem " + str(8 - contador) + " chances\n")

        print("Sua palavra tem", str(len(palavra)),'letras')

        print("\nLetras já inseridas: " + certas + erradas + '\n')
        chute = input("\nFaça seu chute: \n")

        while len(chute) != 1 or chute in troca or chute not in "abcdefghijklmnopqrstuvwxyzçáâãẽêéèàíìõôóòũûúù!@#$%*()_+='/?º[]''-|\/\/;:.><,":
            print("Digite apenas letras e não as repita!!!")
            chute = input("Faça seu chute: \n")

        if chute in palavra:
            troca = ''
            certas += chute
            for chute in palavra:

                if chute in certas:
                    troca += chute
                else:
                    troca += '_'
        else:
                contador += 1
                erradas += chute
                print('\n\n',"""
                            .oPYo.
                            8.
                            `boo   oPYo. oPYo. .oPYo. o    o
                            .P     8  `' 8  `' 8    8 8    8
                            8      8     8     8    8 8    8
                            `YooP' 8     8     `YooP' `YooP'
                            :.....:..::::..:::::.....::.....:
                            :::::::::::::::::::::::::::::::::
                            :::::::::::::::::::::::::::::::::
                                                            """)
        desenha(erradas)
        print('\n',troca,'\n')

    if sorted(certas) != sorted(palavra):
        print('\n\n A palavra correta era:',palavra)
        resposta = input("Você deseja jogar novamente ? \n")
        jogar_novamente(resposta)


forca()
