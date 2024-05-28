vet = []

n = int(input('Digite a quantidade de nomes:  '))

for i in range(n):
    vet.append(input(f'Digite o {i+1}° nome: '))


print('Os nomes pares são: ')
for i in range(n):
    if len(vet[i]) % 2 == 0:
        print(f'{vet[i]} tem {len(vet[i])} letras ')