vet = []
vet_semdupli = []

n = int(input('Digite a quantidade numeros: '))

for i in range(n):
    elemento = int(input(f"Digite o elemento {i+1} da lista: "))
    vet.append(elemento)

for elemento in vet:
    if elemento not in vet_semdupli:
        vet_semdupli.append(elemento)

print(f'A lista completa é {vet}, porem ela sem duplicatas é {vet_semdupli}')
    