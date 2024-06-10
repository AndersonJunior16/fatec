temp = []

for i in range(7):
    temp.append(float(input(f'Digite a temperatura maxima do {i+1} dia: ')))


solicitacao = int(input('Digite o dia que você quer ver a temperatura: (de 1 a 7)'))

while solicitacao > 7:
    print('O numero digitado está incorreto')
else:
    solicitacao = int(input('Digite novamente: '))