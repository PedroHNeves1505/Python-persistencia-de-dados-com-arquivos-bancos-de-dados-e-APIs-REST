# Arquivos .txt

# Cria e escreve a mensagem indicada no txt
with open('Modulo_2_arquivos/dados.txt', 'w') as arquivo:
    arquivo.write('Hello World')

# Abre e lê o arquivo txt indicado
with open('Modulo_2_arquivos/dados.txt', 'r') as arquivo:
    conteudo_arquivo = arquivo.read()
print(conteudo_arquivo)

# =~=~=~=~==~=~=~=~==~=~=~=~==~=~=~=~==~=~=~=~==~=~=~=~=~ 
# Arquivos .csv
import csv

# Cria e adiciona informações no arquivo .csv indicado
with open('Modulo_2_arquivos/dados.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['nome', 'idade', 'nota'])
    writer.writerow(['pedro', 19, 10])

# Faz a leitura do arquivo .csv indicado
with open('Modulo_2_arquivos/dados.csv', newline='') as f:
    reader = csv.reader(f)
    for linha in reader:
        print(linha)

# =~=~=~=~==~=~=~=~==~=~=~=~==~=~=~=~==~=~=~=~==~=~=~=~=~ 
# Arquivos .json
import json

dados = {'nome':'pedro', 'idade': 19, 'enderecos':['a,', 'b']}

# Cria o .json e tranforma o dict dados em .json
with open('Modulo_2_arquivos/dados.json', 'w') as f:
    json.dump(dados, f)

# Faz a leitura do arquico .csv
with open('Modulo_2_arquivos/dados.json', 'r') as f:
    load = json.load(f)
    print(load)