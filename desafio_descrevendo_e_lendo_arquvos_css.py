# Crie um programa que grave em um arquivo alunos.csv uma lista de alunos e suas notas.
# Leia o arquivo alunos.csv e imprima apenas os alunos com nota maior ou igual a 7.0.
import csv

nomes = []
notas = []
aluno = []

while True:
    nome = input('Digite o nome do aluno: ')
    nota = input('Digite sua nota: ')
    nomes.append(nome)
    notas.append(nota)
    aluno.append([nome, nota])
    continuar  = input('Deseja adicionar outro aluno? (s/n): ')
    if continuar == 'n':
        break

with open('desafio.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(aluno)

with open('desafio.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    alunos_acima_media = []
    for aluno in reader:
        nome = aluno[0]
        nota = float(aluno[1])
        if nota > 7:
            alunos_acima_media.append(aluno)

for aluno in alunos_acima_media:
    print(f'{aluno[0]} - {aluno[1]}')