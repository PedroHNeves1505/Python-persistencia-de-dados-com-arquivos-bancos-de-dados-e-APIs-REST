filmes_fav = ['Homem de Ferro', 'Capitão America', 'Vingadores Guerra Infinita', 'Vingadores Ultimato']
datas_filmes = '1/08/2019', '23/4/2018', '22/07/2023', '07/07/2025'
dicionario_filmes = {}

for i in range(len(filmes_fav)):
    dicionario_filmes[filmes_fav[i]] = datas_filmes[i]

print(f'{'Fimes Favoritos':<27} --- Data ')
for key, value in dicionario_filmes.items():
    print(f'{key:<27} --- {value}')