### Membros:
- Murilo Cordeiro Ferreira - RM 556727
- Vitor Augusto - RM 555469
- Geronimo Augusto - RM 557170

---

# 📘 **README — Projeto: Soluções para o Problema da Mochila (Knapsack 0/1)**

Este projeto implementa e compara quatro abordagens clássicas para resolver o **Problema da Mochila 0/1 (0/1 Knapsack Problem)** aplicadas ao contexto de **otimização de portfólio de projetos**, onde existe um limite máximo de horas-especialista disponíveis.

O objetivo é determinar **quais projetos devem ser selecionados** para **maximizar o valor total**, sem ultrapassar a capacidade total de horas.

As quatro abordagens implementadas são:

1. **Algoritmo Guloso (Greedy)**
2. **Solução Recursiva Pura**
3. **Programação Dinâmica Top-Down (Memoização)**
4. **Programação Dinâmica Bottom-Up (Iterativa)**

O projeto também inclui uma **bateria de testes** para cada método, incluindo um caso especial onde o método Greedy falha — e essa falha é importante para fins acadêmicos.

---

## 📂 **Estrutura do Projeto**

```
/seu_projeto
│
├── base.py      # Arquivo contendo todas as funções e testes
└── README.md       # Este arquivo
```

Não há outras pastas ou dependências.

---

## 📌 **Descrição das Abordagens**

### 🔹 1. Greedy (Guloso)

Seleciona projetos pela maior **densidade de valor** (valor dividido pelas horas).
Simples e rápido, mas **não garante solução ótima** no Knapsack 0/1.

📉 Complexidade: **O(n log n)**
⚠ Pode falhar em casos específicos.

---

### 🔹 2. Recursiva Pura

Explora todas as combinações de forma exaustiva.

📉 Complexidade: **O(2ⁿ)**
⚠ Lenta, usada apenas para estudo teórico.

---

### 🔹 3. DP Top-Down (Memoização)

Versão otimizada da recursiva, armazenando subproblemas já resolvidos.

📈 Complexidade: **O(n · C)**
✔ Eficiente e fácil de entender.

---

### 🔹 4. DP Bottom-Up (Iterativa)

Constrói uma tabela com subsoluções de forma iterativa.

📈 Complexidade: **O(n · C)**
🔝 Geralmente a abordagem mais estável e performática.

---

## 🧪 **Casos de Teste**

Cada função possui quatro casos de teste.
Um deles é **especialmente projetado para fazer o algoritmo Greedy falhar**:

```python
projetos_bug = [
    ("A", 60, 10),  # Maior densidade
    ("B", 100, 20)  # Maior valor total (ótimo)
]
capacidade = 20
```

Greedy escolhe A → valor = 60
Ótimo verdadeiro = B → valor = 100
As demais abordagens corrigem esse resultado.

---

## 🧰 **Requisitos**

Nenhuma dependência externa.

✔ **Python 3.8+**
✔ Funciona em Windows, Linux ou Mac

---

## ▶️ **Como Executar**

1. Abra o terminal na pasta do projeto.
2. Execute:

```
python base.py
```

3. O programa irá:

* Rodar todos os testes
* Comparar os valores obtidos
* Mostrar onde Greedy falha
* Mostrar que memoização e bottom-up encontram o valor ótimo

---

## 📊 **Saída Esperada (resumo)**

```
======================
     TESTES GREEDY
======================
[Greedy] Caso Especial – (FALHA ESPERADA):
(60, 10, ['A'])

======================
    TESTES BOTTOM-UP
======================
[Bottom-Up] Caso Especial – (corrige Greedy):
100
```