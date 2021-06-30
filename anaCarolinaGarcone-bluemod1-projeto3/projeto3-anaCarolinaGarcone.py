# Projeto 03 – Simulador de Votação
# Crie um programa que simule um sistema de votação, ele deve receber votos
# até que o usuário diga que não tem mais ninguém para votar, esse programa
# precisa ter duas funções:
# #######A 1° Função autoriza_voto() parâmetro o ano de nascimento de uma pessoa digitado pelo usuário,
# #######retornando voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
# A 2° Função votacao() dois parâmetros, autorização (que
# virá da função autoriza_voto()) e o voto que é o número que a pessoa votou.
# Se ela não puder votar, votacao() retorna “Você não pode votar”,
# caso o contrário votacao() deve validar o número que a pessoa escolheu 
# (crie 3 candidatos para a votação) pode escolher de 1 a 5:
# 1, 2 ou 3 - Votos para os respectivos candidatos
# 4- Voto Nulo
# 5 - Voto em Branco
# votacao() tem que calcular e mostrar:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# Qual candidato venceu a votação.

# as funções tem que ser criadas primeiro

def autorizaVoto(anoDeNascimento) :

    from datetime import date

    anoAtual = date.today().year # pegar o ano atual 
    calculoAno = anoAtual - anoDeNascimento

    if calculoAno >= 18 and calculoAno <= 70 :
        return 'obrigatorio'
    elif calculoAno == 16 or calculoAno == 17 and calculoAno > 70 :
        return 'opcional'
    elif calculoAno < 16 :
        return 'negado'


def votacao(autorizacao, voto) :
    if autorizaVoto(autorizacao) == 'negado' :
        return 'Você não pode votar.'
    
    else  :
        #validar o numero que foi escolhido
        
        if voto == 'Batman' :
            return 'Batman'
        elif voto == 'Superman' :
            return 'Superman'
        elif voto == 'Mulher Maravilha' :
            return 'Mulher Maravilha'
        elif voto == 'Nulo' :
            return 'Nulo'
        elif voto == 'Branco' :
            return 'Branco'
        else :
            return 'Voto inválido.'

from collections import Counter

import operator


lista = []

while True :

    inicioOuFIm = input('Instruções para o seu voto: \na. Digite o nome de seu candidato. \nb. Confira se foi digitado certo e confirme. \nc. Para o voto em branco ou nulo é só digitar e confirmar. \nVOTE CONSCIENTE. [OK] para prosseguir:  ')
    print()

    while inicioOuFIm != 'Sair' :
        
        escolhendo = 'Sem Voto'
        ano = int(input('Seu ano de nascimento: '))
        print()

        retornoFuncao1 = autorizaVoto(ano) # vai retornar obrigatorio/opcional/negado
        if retornoFuncao1 != 'negado' :
            escolhendo = input('Opções: \n[Batman].......... \n[Mulher Maravilha] \n[Superman]........ \n[Nulo]............ \n[Branco]..........\nDigite seu voto: ').lower().title()
            retornoFuncao2 = votacao(ano, escolhendo) # vai retornar as opcoes de voto
            if retornoFuncao2 != 'Voto inválido.' :
                lista.append(escolhendo)
            else :
                print()
                print(retornoFuncao2) # se cair no else vai retornar voto invalido
        else :
            print(votacao(ano,escolhendo)) # se o retornoFuncao1 for 'negado' entao vai sair no else e retornar que nao pode votar

        print()
        inicioOuFIm = input('digite [Sair] para os resultados ou [Continuar] para mais votos: ').lower().title()
        print()
    
    votados = dict(Counter(lista)) #aqui eu consigo organizar em um dicionario todos os votos

    for i, v in votados.items():
        print(f'O total de votos para {i} é de: {v}') #aqui eu printo o total de cada voto com um for 
    
    print()

    remover_itens = []

    for chave, valor in votados.items():
        if chave == 'Nulo' or chave == 'Branco' : # depois de printar o total de cada voto, eu removi o nulo e o branco para trabalhar so com os candidatos e printar o vencedor
            remover_itens.append(chave)

    for item in remover_itens:
        votados.pop(item)
    
    vencedor = max(votados.items(), key=operator.itemgetter(1))[0] # aqui vou guardar quem é o vencedor 
    empate = votados.get(str(vencedor)) # vot pegar o valor do vencedor 
    print('O(s) vencedor(es) é(säo): ')
    print()


    quantidadeMulherMaravilha = votados.get('Mulher Maravilha')
    quantidadeBatman = votados.get('Batman')
    quantidadeSuperman = votados.get('Superman')
    #aqui eu peguei a quantidade de votos de cada candidato para verificar

    if empate == quantidadeMulherMaravilha :
        print(f'Mulher Maravilha com {quantidadeMulherMaravilha} votos')
    if empate == quantidadeBatman :
        print(f'Batman com {quantidadeBatman} votos')
    if empate == quantidadeSuperman :
        print(f'Superman com {quantidadeSuperman} votos')

    # aqui eu verificar se tem mais de um vencedor 
    break

# professor, talvez eu codigo ficou meio bagunçado e não sei se está dando para entender bem. 
# Eu tentei muito deixar um codigo mais pequeno e claro, mas não sei se ficou bom.
# mas eu gostei muito, consegui aprender varias coisas novas pesquisando para resolver os problemas que surgiam 