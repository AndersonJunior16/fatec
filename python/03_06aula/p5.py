n = int(input('Digite a quantidade de numeros: '))
vet = [''] * n


for i in range(n):
    nomes = input(f'Digite {i+1}° nome: ')
    vet[i] = nomes


for i in range(n):
    if i % 2 == 0:
        print(f'Na posição {i}(par) está o nome {vet[i]}')
    elif i % 2 == 1:
        print(f'Na posição {i}(impar) está o nome {vet[i]}')
