# Projeto 02 – Jogo Jokenpô
# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.

import random 
aleatorio = ['pedra', 'papel', 'tesoura']

while True :
    contComputador = 0
    contEscolha = 0
    contEmpate = 0

    rodadas = int(input('Quantas rodadas? '))

    for i in range(rodadas) :

        escolha = input('pedra, papel ou tesoura? ')
        computador = (random.choice(aleatorio))

        if escolha == 'pedra' :
            if computador == 'tesoura' :
                contEscolha += 1
            elif computador == 'papel' :
                contComputador += 1
            else : 
                contEmpate += 1


        elif escolha == 'tesoura' :
            if computador == 'pedra' :
                contComputador += 1
            elif computador == 'papel' :
                contEscolha += 1
            else : 
                contEmpate += 1


        elif escolha == 'papel' :
            if computador == 'tesoura' :
                contComputador += 1
            elif computador == 'pedra' :
                contEscolha += 1
            else : 
                contEmpate += 1
        
        print(f'O computador escolheu {computador}.')
    
    print()
    if contEscolha > contComputador :
        print('O grande campeão foi você!')
    else :
        print('O grande campeão foi o computador!') 

    print()   
    print(f'Você ganhou {contEscolha} vez(es).')
    print(f'Computador ganhou {contComputador} vez(es).')
    print(f'Foram {contEmpate} empate(s).')
    print()
    
    jogarNovamente = input('Deseja jogar novamente? [SIM/NAO]')
    if jogarNovamente == 'NAO' or jogarNovamente == 'nao' :
        break
    

# professor, ainda não tenho certeza se esse foi o jeito mais facil de fazer, mas eu consegui
# pensar mais rapido em como eu faria e fiquei bem feliz.
# professor, nesse projeto eu não tive tempo de colocar contra erro de usuario, mas nos proximos 
# eu vou melhorar isso.
# adorei fazer esse projeto, obrigada!!
