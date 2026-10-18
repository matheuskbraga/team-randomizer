import os
import random


os.system('cls')

lista_alunos = []
matriz_grupos = []

with open("alunos.txt", "r", encoding="utf-8") as alunos:
    for aluno in alunos:  
        lista_alunos.append(aluno.strip())


tamanho_lista_alunos = len(lista_alunos)    # tamanho da turma
tamanho_equipes = int(input("Digite o tamanho da equipe: ")) # tamanho dos grupos que eu quero


while len(lista_alunos) > 0:
    lista_grupo_separacao = []
    for x in range(tamanho_equipes):
        if len(lista_alunos) == 0:
            matriz_grupos[x].append(lista_grupo_separacao)
            break
        pessoa_aleatoria = random.choice(lista_alunos) # pega uma pessoa aleatoria da lista
        lista_grupo_separacao.append(pessoa_aleatoria) # adiciona no grupo
        lista_alunos.remove(pessoa_aleatoria)          # remove da lista da turma de quem tem que fazer o grupo
    if len(lista_alunos) == 0:
        break
    matriz_grupos.append(lista_grupo_separacao)


print(matriz_grupos)