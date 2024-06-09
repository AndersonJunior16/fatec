notas = []
 
for i in range(5):
    notas.append(float(input(f'Digite a {i+1}º nota do aluno: ')))

print(f'As notas são: {notas}')
print('Altere a terceira nota do aluno: ')
nota_3 = float(input(''))

notas[2] = nota_3

print(f'As novas notas são {notas}')