import random

def gerar_listas(tamanho):
    lista_ordenada = list(range(1, tamanho + 1))
    lista_inversa = list(range(tamanho, 0, -1))
    lista_aleatoria = lista_ordenada[:]
    random.shuffle(lista_aleatoria)
    return lista_ordenada, lista_inversa, lista_aleatoria

def salvar_listas(tamanho):
    lista_ordenada, lista_inversa, lista_aleatoria = gerar_listas(tamanho)
    nome_arquivo = f'lista_{tamanho}.txt'
    with open(nome_arquivo, 'w') as f:
        f.write(', '.join(map(str, lista_ordenada)) + '\n')
        f.write(', '.join(map(str, lista_inversa)) + '\n')
        f.write(', '.join(map(str, lista_aleatoria)) + '\n')

for tamanho in [1000, 10000, 50000, 100000]:
    salvar_listas(tamanho)
    print(f"Arquivo 'lista_{tamanho}.txt' gerado com sucesso!")