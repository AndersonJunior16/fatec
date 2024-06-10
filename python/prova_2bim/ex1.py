vet = []

n = int(input('Digite a quantidade de nomes: '))

for i in range(n):
    vet.append(str(input(f'Digite o {i+1} nome: ')))

print(f'A lista de nomes invertida é {vet[::-1]}')