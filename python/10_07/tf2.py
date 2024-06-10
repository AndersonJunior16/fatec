contatos = []

for i in range(6):
    contatos.append(str(input(f'Digite o {i+1}º contato: ')))

print(f'Os contatos são: {contatos}')
troca_cont = str(input('Substitua o quinto nome por "Elisa": '))

contatos[4] = troca_cont
print(f'Os contatos atualizados são: {contatos}')