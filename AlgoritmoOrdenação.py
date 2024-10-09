import time
import sys

sys.setrecursionlimit(100000)

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    comparacoes, trocas = 0, 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
    return comparacoes, trocas

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    comparacoes, trocas = 0, 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparacoes += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            trocas += 1
    return comparacoes, trocas

# Insertion Sort
def insertion_sort(arr):
    comparacoes, trocas = 0, 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        comparacoes += 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            trocas += 1
            j -= 1
            comparacoes += 1
        arr[j + 1] = key
    return comparacoes, trocas

# Merge Sort
def merge_sort(arr):
    comparacoes, trocas = [0], [0]

    def merge(arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = arr[l:m+1]
        R = arr[m+1:r+1]

        i = j = 0
        k = l

        while i < n1 and j < n2:
            comparacoes[0] += 1
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def sort(arr, l, r):
        if l < r:
            m = (l + r) // 2
            sort(arr, l, m)
            sort(arr, m + 1, r)
            merge(arr, l, m, r)

    sort(arr, 0, len(arr) - 1)
    return comparacoes[0], 0

# Quick Sort
def quick_sort(arr):
    comparacoes, trocas = [0], [0]

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparacoes[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas[0] += 1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        trocas[0] += 1
        return i + 1

    def sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            sort(arr, low, pi - 1)
            sort(arr, pi + 1, high)

    sort(arr, 0, len(arr) - 1)
    return comparacoes[0], trocas[0]

# Heap Sort
def heapify(arr, n, i, comparacoes, trocas):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        comparacoes[0] += 1
        if arr[left] > arr[largest]:
            largest = left

    if right < n:
        comparacoes[0] += 1
        if arr[right] > arr[largest]:
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        trocas[0] += 1
        heapify(arr, n, largest, comparacoes, trocas)

def heap_sort(arr):
    n = len(arr)
    comparacoes, trocas = [0], [0]

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, comparacoes, trocas)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        trocas[0] += 1
        heapify(arr, i, 0, comparacoes, trocas)

    return comparacoes[0], trocas[0]

def ler_lista(filename, tipo_distribuicao):
    try:
        with open(filename, 'r') as f:
            listas = f.read().splitlines()
            if tipo_distribuicao == 1:
                return [int(x) for x in listas[0].split(',')]
            elif tipo_distribuicao == 2:
                return [int(x) for x in listas[1].split(',')]
            else:
                return [int(x) for x in listas[2].split(',')]
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
        return None

def executar_teste():
    tamanhos = {1: "1000", 2: "10000", 3: "50000", 4: "100000"}
    distrib = {1: "Ordenada", 2: "Inversamente Ordenada", 3: "Aleatória"}

    while True:
        print("Selecione o tamanho da lista:")
        for key, value in tamanhos.items():
            print(f"{key} - {value} elementos")

        try:
            tam_escolhido = int(input())
            if tam_escolhido not in tamanhos:
                print("Opção inválida! Por favor, selecione uma opção válida.")
                continue
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
            continue

        print("Selecione a distribuição da lista:")
        for key, value in distrib.items():
            print(f"{key} - {value}")

        try:
            dist_escolhida = int(input())
            if dist_escolhida not in distrib:
                print("Opção inválida! Por favor, selecione uma opção válida.")
                continue
        except ValueError:
            print("Entrada inválida! Por favor, insira um número.")
            continue

        filename = f"lista_{tamanhos[tam_escolhido]}.txt"
        lista = ler_lista(filename, dist_escolhida)

        if lista is None:
            print("Erro: Nenhuma lista encontrada. Tente novamente.")
            return

        algoritmos = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort]

        for algoritmo in algoritmos:
            lista_copia = lista[:]
            inicio = time.time()
            comparacoes, trocas = algoritmo(lista_copia)
            tempo_execucao = (time.time() - inicio) * 1000

            print(f"Algoritmo {algoritmo.__name__}:")
            print(f"Tempo de execução: {tempo_execucao:.3f} ms")
            print(f"Comparações: {comparacoes}, Trocas: {trocas}")
            print()

        break

executar_teste()
