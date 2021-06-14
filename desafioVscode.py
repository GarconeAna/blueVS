print('olá, eu sou o detetive no caso do assassinato ocorrido. \nQuero fazer algumas perguntas para você.')
print('')

pontos = 0

resp = input('Você telefonou para a vítima? [SIM/NÃO] ')
resp = resp.upper()
while resp == 'SIM' or resp == 'S' :
    pontos += 1
    break

resp = input('Você esteve no local do crime? [SIM/NÃO] ')
resp = resp.upper()
while resp == 'SIM' or resp == 'S' :
    pontos += 1
    break

resp = input('Você mora perto da vítima? [SIM/NÃO] ')
resp = resp.upper()
while resp == 'SIM' or resp == 'S' :
    pontos += 1
    break

resp = input('Você devia para a vítima? [SIM/NÃO] ')
resp = resp.upper()
while resp == 'SIM' or resp == 'S' :
    pontos += 1
    break

resp = input('Você já trabalhou com a vítima? [SIM/NÃO] ')
resp = resp.upper()
while resp == 'SIM' or resp == 'S' :
    pontos += 1
    break


if pontos <= 1 : 
    print('Inocente, está liberado.') 
elif pontos == 2 :
    print('Suspeito, vamos ficar de olho em você.')
elif pontos <= 4 :
    print('Cúmplice, conte agora quem é o assassino.')
elif pontos == 5 :
    print('ASSASSINO, VOCÊ ESTÁ PRESO.')
