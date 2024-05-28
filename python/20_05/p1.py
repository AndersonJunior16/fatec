vet_consoante = []
consoantes = 'BCDFGHJKLMNPQRSTVWXYZ'

for i in range(10):
    letra = input(f'Digite a {i+1}° letra: ').upper()
    vet_consoante.append(letra)

consoante_count = sum(vet_consoante.count(consoante) for consoante in consoantes)

print(f'Existem {consoante_count} consoantes escritas')