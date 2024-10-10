import time
import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

sys.setrecursionlimit(10000000)

# Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    comparacoes, trocas = 0, 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocas += 1
    return comparacoes, trocas

# Selection Sort
def selection_sort(lista):
    n = len(lista)
    comparacoes, trocas = 0, 0
    for i in range(n):
        indice_minimo = i
        for j in range(i+1, n):
            comparacoes += 1
            if lista[j] < lista[indice_minimo]:
                indice_minimo = j
        if indice_minimo != i:
            lista[i], lista[indice_minimo] = lista[indice_minimo], lista[i]
            trocas += 1
    return comparacoes, trocas

# Insertion Sort
def insertion_sort(lista):
    comparacoes, trocas = 0, 0
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        comparacoes += 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            trocas += 1
            j -= 1
            comparacoes += 1
        lista[j + 1] = chave
    return comparacoes, trocas

# Merge Sort
def merge_sort(lista):
    comparacoes, trocas = [0], [0]
    
    def mesclar(lista, esquerda, meio, direita):
        n1 = meio - esquerda + 1
        n2 = direita - meio
        
        L = lista[esquerda:meio+1]
        R = lista[meio+1:direita+1]
        
        i = j = 0
        k = esquerda
        
        while i < n1 and j < n2:
            comparacoes[0] += 1
            if L[i] <= R[j]:
                lista[k] = L[i]
                i += 1
            else:
                lista[k] = R[j]
                j += 1
            k += 1
            
        while i < n1:
            lista[k] = L[i]
            i += 1
            k += 1
            
        while j < n2:
            lista[k] = R[j]
            j += 1
            k += 1
    
    def ordenar(lista, esquerda, direita):
        if esquerda < direita:
            meio = (esquerda + direita) // 2
            ordenar(lista, esquerda, meio)
            ordenar(lista, meio + 1, direita)
            mesclar(lista, esquerda, meio, direita)
    
    ordenar(lista, 0, len(lista) - 1)
    return comparacoes[0], 0

# Quick Sort
def quick_sort(lista):
    comparacoes, trocas = [0], [0]
    
    def particionar(lista, baixo, alto):
        pivo = lista[alto]
        i = baixo - 1
        for j in range(baixo, alto):
            comparacoes[0] += 1
            if lista[j] < pivo:
                i += 1
                lista[i], lista[j] = lista[j], lista[i]
                trocas[0] += 1
        lista[i+1], lista[alto] = lista[alto], lista[i+1]
        trocas[0] += 1
        return i + 1
    
    def ordenar(lista, baixo, alto):
        if baixo < alto:
            pi = particionar(lista, baixo, alto)
            ordenar(lista, baixo, pi - 1)
            ordenar(lista, pi + 1, alto)
    
    ordenar(lista, 0, len(lista) - 1)
    return comparacoes[0], trocas[0]

# Heap Sort
def heapify(lista, n, i, comparacoes, trocas):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    if esquerda < n:
        comparacoes[0] += 1
        if lista[esquerda] > lista[maior]:
            maior = esquerda

    if direita < n:
        comparacoes[0] += 1
        if lista[direita] > lista[maior]:
            maior = direita

    if maior != i:
        lista[i], lista[maior] = lista[maior], lista[i]
        trocas[0] += 1
        heapify(lista, n, maior, comparacoes, trocas)

def heap_sort(lista):
    n = len(lista)
    comparacoes, trocas = [0], [0]

    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i, comparacoes, trocas)

    for i in range(n - 1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        trocas[0] += 1
        heapify(lista, i, 0, comparacoes, trocas)

    return comparacoes[0], trocas[0]

def ler_lista(nome_arquivo, tipo_distribuicao):
    try:
        with open(nome_arquivo, 'r') as f:
            listas = f.read().splitlines()
            if tipo_distribuicao == 1:
                return [int(x) for x in listas[0].split(',')]
            elif tipo_distribuicao == 2:
                return [int(x) for x in listas[1].split(',')]
            else:
                return [int(x) for x in listas[2].split(',')]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

def plotar_analise_ordenacao(df_resultados):
    # Plots separados para tempo de execução por distribuição
    distribuicoes = df_resultados['Distribuição'].unique()
    tamanhos = df_resultados['Tamanho Lista'].unique()
    
    # Gráfico de tempo de execução
    plt.figure(figsize=(15, 5*len(distribuicoes)))
    
    for idx, dist in enumerate(distribuicoes, 1):
        plt.subplot(len(distribuicoes), 1, idx)
        
        for tamanho in tamanhos:
            dados = df_resultados[
                (df_resultados['Distribuição'] == dist) & 
                (df_resultados['Tamanho Lista'] == tamanho)
            ]
            
            if not dados.empty:
                plt.bar(
                    [f"{algo}\n({tamanho} elementos)" for algo in dados['Algoritmo']], 
                    dados['Tempo de Execução (ms)'],
                    label=f'Lista {tamanho}'
                )
        
        plt.title(f'Tempo de Execução - Distribuição {dist}')
        plt.xlabel('Algoritmos')
        plt.ylabel('Tempo (ms)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        if len(tamanhos) > 1:
            plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Gráfico de comparações e trocas
    plt.figure(figsize=(15, 5*len(distribuicoes)))
    
    for idx, dist in enumerate(distribuicoes, 1):
        plt.subplot(len(distribuicoes), 1, idx)
        
        for tamanho in tamanhos:
            dados = df_resultados[
                (df_resultados['Distribuição'] == dist) & 
                (df_resultados['Tamanho Lista'] == tamanho)
            ]
            
            if not dados.empty:
                x = np.arange(len(dados['Algoritmo']))
                largura = 0.35 / len(tamanhos)
                deslocamento = largura * (list(tamanhos).index(tamanho) - (len(tamanhos)-1)/2)
                
                plt.bar(
                    x + deslocamento, 
                    dados['Comparações'],
                    largura,
                    label=f'Comparações ({tamanho} elementos)',
                    alpha=0.7
                )
                plt.bar(
                    x + deslocamento, 
                    dados['Trocas'],
                    largura,
                    bottom=dados['Comparações'],
                    label=f'Trocas ({tamanho} elementos)',
                    alpha=0.7
                )
                
                plt.xticks(x, dados['Algoritmo'], rotation=45)
        
        plt.title(f'Comparações e Trocas - Distribuição {dist}')
        plt.xlabel('Algoritmos')
        plt.ylabel('Quantidade de Operações')
        plt.grid(True, alpha=0.3)
        plt.legend()
    
    plt.tight_layout()
    plt.show()

def executar_teste():
    tamanhos = {1: "1000", 2: "10000", 3: "50000", 4: "100000"}
    distribuicoes = {1: "Ordenada", 2: "Inversamente Ordenada", 3: "Aleatória"}
    
    resultados = []
    
    print("Selecione os tamanhos das listas (separados por espaço):")
    for chave, valor in tamanhos.items():
        print(f"{chave} - {valor} elementos")
    
    tam_escolhidos = list(map(int, input().split()))
    
    print("Selecione as distribuições das listas (separadas por espaço):")
    for chave, valor in distribuicoes.items():
        print(f"{chave} - {valor}")
    
    dist_escolhidas = list(map(int, input().split()))
    
    algoritmos = [bubble_sort, selection_sort, insertion_sort, 
                 merge_sort, quick_sort, heap_sort]
    
    for tam in tam_escolhidos:
        for dist in dist_escolhidas:
            nome_arquivo = f"lista_{tamanhos[tam]}.txt"
            lista = ler_lista(nome_arquivo, dist)
            
            if lista is None:
                continue
                
            for algoritmo in algoritmos:
                lista_copia = lista[:]
                inicio = time.time()
                comparacoes, trocas = algoritmo(lista_copia)
                tempo_execucao = (time.time() - inicio) * 1000
                
                resultados.append({
                    'Algoritmo': algoritmo.__name__,
                    'Tempo de Execução (ms)': tempo_execucao,
                    'Comparações': comparacoes,
                    'Trocas': trocas,
                    'Tamanho Lista': tamanhos[tam],
                    'Distribuição': distribuicoes[dist]
                })
                
                print(f"\nAlgoritmo {algoritmo.__name__} - Lista {tamanhos[tam]} - {distribuicoes[dist]}:")
                print(f"Tempo de execução: {tempo_execucao:.3f} ms")
                print(f"Comparações: {comparacoes}, Trocas: {trocas}")
    
    # Criação do DataFrame com os resultados
    df_resultados = pd.DataFrame(resultados)
    
    # Exibição da tabela no console
    print("\nResultados dos Algoritmos:")
    pd.set_option('display.float_format', lambda x: '{:.6f}'.format(x))
    print(df_resultados[['Algoritmo', 'Tempo de Execução (ms)', 'Comparações', 'Trocas', 'Tamanho Lista', 'Distribuição']])
    print("\n")
    
    plotar_analise_ordenacao(df_resultados)

if __name__ == "__main__":
    executar_teste()