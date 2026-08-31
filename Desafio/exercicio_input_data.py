nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

with open('input_data.txt', 'w', newline='') as f:
    f.write(f'{nome}\n')
    f.write(f'{idade}\n')

with open('input_data.txt', 'r', newline='') as f:
    for linha in f:
        print(linha.strip())