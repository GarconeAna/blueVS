#Desafio01 

# professor, eu demorei um pouco para pensar em como guardaria a resposta do usuario e depois contar elas
# eu pensei varios jeitos diferente, queria tambem deixar um codigo menor. Esse jeito foi o que conseguir.
# nao sinto que ele esta 100%, mas esta funcionando direitinho
# acho que quando aprendermos mais coisas, vai ficar mais simples resolver os programas

print('olá, eu sou o detetive no caso do assassinato ocorrido. \nQuero fazer algumas perguntas para você.')
print('')
pergunta1 = input('Você telefonou para a vítima? [SIM/NÃO] ') 
pergunta2 = input('Você esteve no local do crime? [SIM/NÃO] ')
pergunta3 = input('Você mora perto da vítima? [SIM/NÃO] ')
pergunta4 = input('Você devia para a vítima? [SIM/NÃO] ')
pergunta5 = input('Você já trabalhou com a vítima? [SIM/NÃO] ')

pgtTratada1 = pergunta1.upper() # eu tentei fazer aqui igual como fiz com o count
pgtTratada2 = pergunta2.upper() # mas dava erro, eu não entendi por que
pgtTratada3 = pergunta3.upper() # não conseguir juntar todos eles em uma variavel 
pgtTratada4 = pergunta4.upper() # e colocar o upper, entao tive que fazer para cada pergunta
pgtTratada5 = pergunta5.upper() # uma variavel tratada

pontos = (pgtTratada1, pgtTratada2, pgtTratada3, pgtTratada4, pgtTratada5).count('SIM')
print('') # esse foi o jeito que conseguir retornar quantos SIM o usuario manda
# tinha feito para cada um e depois ia somar todos os [ponto]

if pontos <= 1 : # a condição foi simples de fazer, depois de conseguir guardar quantos SIM
    print('Inocente, está liberado.') # so precisava printar conforme a quantidade
elif pontos == 2 :
    print('Suspeito, vamos ficar de olho em você.')
elif pontos <= 4 :
    print('Cúmplice, conte agora quem é o assassino.')
elif pontos == 5 :
    print('ASSASSINO, VOCÊ ESTÁ PRESO.')

# professor, eu gostei muito de fazer esse desafio. obrigada pelas suas aulas.