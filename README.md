# Análise Empírica de Algoritmos de Ordenação

Este projeto tem como objetivo realizar uma análise empírica de diferentes algoritmos de ordenação, medindo seu desempenho em termos de tempo de execução, número de comparações e trocas em listas de diferentes tamanhos e distribuições.

## Algoritmos Implementados

Os seguintes algoritmos de ordenação foram implementados e analisados:

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort

## Distribuições das Listas

As listas geradas para os testes podem ser das seguintes distribuições:

1. **Ordenada**
2. **Inversamente Ordenada**
3. **Aleatória**

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/uGonzaguinha/Trabalho_de_Ordenacao_de_Algoritmos.git
   cd seu_repositorio

2. Gere as listas::
   ```bash
   python GerarLista.py

3. Execute os testes de ordenação::
   ```bash
   python AlgoritmoOrdenação.py
   
## Resultados
Os resultados da execução incluem:

- Tempo de execução de cada algoritmo em milissegundos.
- Número de comparações realizadas.
- Número de trocas realizadas.
- Tabelas e Gráficos comparativos do desempenho de cada algoritmo para diferentes tamanhos e distribuições de listas.