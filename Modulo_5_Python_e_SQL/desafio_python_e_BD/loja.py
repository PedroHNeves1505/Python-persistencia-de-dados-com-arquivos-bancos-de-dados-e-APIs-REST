from funções_loja import criar_tabela_produtos, adicionar_produtos, listar_produtos

criar_tabela_produtos()

print('Adicionando produto ao banco de dados\n')
for i in range(3):
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))
    print(f'{"=~" * 10}')
    adicionar_produtos(nome, preco)

listar_produtos()


