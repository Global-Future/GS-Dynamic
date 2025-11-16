def abordagem_gulosa(projects, capacity):
    """
    projects: lista de tuplas (nome, valor, horas)
    capacity: capacidade máxima de horas (int)
    retorna: (valor_total, horas_usadas, lista_de_projetos_escolhidos)
    """
    # Calcula densidade (valor por hora)
    projetos_com_densidade = []
    for nome, valor, horas in projects:
        densidade = valor / horas
        projetos_com_densidade.append((nome, valor, horas, densidade))

    # Ordena por densidade (V/E) decrescente
    projetos_com_densidade.sort(key=lambda x: x[3], reverse=True)

    horas_restantes = capacity
    valor_total = 0
    escolhidos = []

    # Seleciona projetos enquanto houver capacidade
    for nome, valor, horas, dens in projetos_com_densidade:
        if horas <= horas_restantes:
            escolhidos.append(nome)
            horas_restantes -= horas
            valor_total += valor

    horas_usadas = capacity - horas_restantes
    return valor_total, horas_usadas, escolhidos

def mochila_recursiva(projects, capacity, i):
    """
    projects: lista de tuplas (nome, valor, horas)
    capacity: capacidade restante (int)
    i: índice do projeto atual (int)
    retorna: valor máximo possível considerando os projetos até i
    """
    # Caso base
    if i < 0 or capacity == 0:
        return 0

    nome, valor, horas = projects[i]

    # Se o projeto não cabe, pula ele
    if horas > capacity:
        return mochila_recursiva(projects, capacity, i - 1)

    # Caso contrário, testa as duas opções:
    # 1. Não incluir o projeto
    # 2. Incluir o projeto
    nao_incluir = mochila_recursiva(projects, capacity, i - 1)
    incluir = valor + mochila_recursiva(projects, capacity - horas, i - 1)

    return max(nao_incluir, incluir)

def mochila_memo(projects, capacity, i, memo):
    """
    projects: lista de tuplas (nome, valor, horas)
    capacity: capacidade restante (int)
    i: índice do projeto atual (int)
    memo: dicionário para armazenar subproblemas resolvidos
    retorna: valor máximo possível considerando os projetos até i
    """
    # Caso base
    if i < 0 or capacity == 0:
        return 0

    # Verifica se já foi calculado
    if (i, capacity) in memo:
        return memo[(i, capacity)]

    nome, valor, horas = projects[i]

    # Se o projeto não cabe
    if horas > capacity:
        result = mochila_memo(projects, capacity, i - 1, memo)
    else:
        # Testa incluir ou não incluir
        nao_incluir = mochila_memo(projects, capacity, i - 1, memo)
        incluir = valor + mochila_memo(projects, capacity - horas, i - 1, memo)
        result = max(nao_incluir, incluir)

    # Armazena o resultado antes de retornar
    memo[(i, capacity)] = result
    return result

def mochila_bottom_up(projects, capacity):
    """
    projects: lista de tuplas (nome, valor, horas)
    capacity: capacidade máxima (int)
    retorna: (valor máximo, tabela)
    """
    n = len(projects)

    # Cria matriz (n+1) x (capacity+1) inicializada com 0
    T = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Preenche a tabela
    for i in range(1, n + 1):
        nome, valor, horas = projects[i - 1]
        for c in range(1, capacity + 1):
            if horas > c:
                T[i][c] = T[i - 1][c]
            else:
                T[i][c] = max(T[i - 1][c], valor + T[i - 1][c - horas])

    return T[n][capacity], T


"""
===========================
Análise de Desempenho
===========================

1️. Greedy:
   - Complexidade de tempo: O(n log n) (por causa da ordenação)
   - Complexidade de espaço: O(n)

2. Recursiva Pura:
   - Complexidade de tempo: O(2^n)
   - Complexidade de espaço: O(n) (profundidade da recursão)

3. Top-Down com Memoização:
   - Complexidade de tempo: O(n * C), onde C é a capacidade.
   - Complexidade de espaço: O(n * C) (armazenamento no dicionário + pilha recursiva)

4. Programação Dinâmica Bottom-Up (Iterativa):
   - Complexidade de tempo: O(n * C)
   - Complexidade de espaço: O(n * C) (tabela de DP)

"""




if __name__ == "__main__":
    capacidade = 10
    projetos = [
        ("A", 12, 4),
        ("B", 10, 3),
        ("C", 7, 2),
        ("D", 4, 3),
    ]

    print("=== GREEDY ===")
    valor, horas, escolhidos = abordagem_gulosa(projetos, capacidade)
    print("Valor:", valor, "| Horas usadas:", horas, "| Projetos:", escolhidos)

    print("\n=== RECURSIVA PURA ===")
    melhor_valor = mochila_recursiva(projetos, capacidade, len(projetos) - 1)
    print("Melhor valor:", melhor_valor)

    print("\n=== MEMOIZAÇÃO ===")
    memo = {}
    melhor_valor = mochila_memo(projetos, capacidade, len(projetos) - 1, memo)
    print("Melhor valor:", melhor_valor, "| Subproblemas armazenados:", len(memo))

    print("\n=== BOTTOM-UP (PD Iterativa) ===")
    melhor_valor, tabela = mochila_bottom_up(projetos, capacidade)
    print("Melhor valor:", melhor_valor)
