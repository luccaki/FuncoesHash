# Módulo/Biblioteca de Funções de Espalhamento pelos métodos de Divisão e Multiplicação
from collections import defaultdict


# Função de espalhamento pelo método da divisão
# h(K) = K mod M 
# Recebe dois valores K e M
# K - Um número natural (chave/key)
# M - Um número natural (Recomendado um numero primo não próximo de uma potência de 2)
# Retorna uma lista ordenada com a seguinte sintaxe:
# [X,[Y]], sendo X o valor de h(K) e Y uma lista dos valores K
def divisão(M, K):
    if M < 0:
        raise Exception("Erro: M precisa ser um numero natural")
    saida = defaultdict(list)
    for m in range(M):
        saida[m] = []
    for k in K:
        saida[k % int(M)].append(k);
    return sorted(saida.items())

# Função de espalhamento pelo método da multiplicação
# h(K) = M × ((K × A) mod 1) "Maior inteiro que seja menor que h(K)"
# Recebe três valores K, M e A
# K - Um número natural (chave/key)
# M - Um número natural (Número de posições na tabela)
# A - Uma constante não negativa. 0 < A < 1.
# Retorna uma lista ordenada com a seguinte sintaxe:
# [X,[Y]], sendo X o valor de h(K) e Y uma lista dos valores K 
def multiplicacao(M, K, A):
    if M < 0:
        raise Exception("Erro: M precisa ser um numero natural")
    if A <= 0 or A >=1:
        raise Exception("Erro: A deve ser uma constante não negativa, 0 < A < 1")
    saida = defaultdict(list)
    for m in range(M):
        saida[m] = []
    for k in K:
        saida[int(((k * A) - int(k * A)) * M)].append(k);
    return sorted(saida.items())
