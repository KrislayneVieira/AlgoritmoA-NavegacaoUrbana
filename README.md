# 🗺️ Algoritmo A* - Navegação Urbana

## 📖 Sobre o Projeto

**Problema**: Sistema de navegação que encontra o caminho mais curto entre dois pontos de uma cidade.

**Solução**: Implementação do algoritmo A* com heurística euclidiana para busca otimizada de rotas.

---

## 🚀 Como Executar

### 1. Instalar Dependências
```bash
pip install networkx matplotlib
```

### 2. Executar o Programa
```bash
python profundidade.py
```

### 3. Resultado Esperado
- **Relatório no terminal** com caminho encontrado e comparação de algoritmos
- **Visualização gráfica** do mapa e rota otimizada

---

## 💡 Como Funciona

### Mapa da Cidade
9 locais conectados: Casa → Padaria → Mercado → Escola → Hospital → Farmácia → Banco → Centro → Parque

### Algoritmo A*
- **Função**: `f(n) = g(n) + h(n)`
- **g(n)**: Custo real até o nó atual
- **h(n)**: Heurística (distância euclidiana até o destino)
- **Garantia**: Solução ótima com heurística admissível

### Comparação de Algoritmos
| Algoritmo | Descrição | Otimalidade |
|-----------|-----------|-------------|
| **A*** | Com heurística euclidiana | ✅ Garantida |
| **Dijkstra** | A* sem heurística | ✅ Garantida |
| **BFS** | Busca em largura simples | ❌ Não garantida |

---

## 📊 Exemplo de Saída

```
🗺️  ALGORITMO A* - NAVEGAÇÃO URBANA
==================================================
🎯 Busca: Casa → Parque
📍 Caminho: Casa → Mercado → Escola → Farmacia → Parque
💰 Custo: 10.47 unidades
🔢 Passos: 5 nós
🧮 Heurística inicial: 8.06

📊 COMPARAÇÃO DE ALGORITMOS:
-----------------------------------
      A*: Custo=10.47 | Nós=5
Dijkstra: Custo=10.47 | Nós=5
     BFS: Custo=10.47 | Nós=5

✅ Heurística Admissível: SIM
✅ Solução Ótima: GARANTIDA
```

---

## 🎯 Funcionalidades Implementadas

### ✅ Requisitos Atendidos
- [x] **Modelagem como grafo** - Cidade com coordenadas reais
- [x] **Implementação A*** - Com heurística personalizada  
- [x] **Demonstração** - Execução automática e visual
- [x] **Comparação** - A*, Dijkstra, BFS lado a lado
- [x] **Visualização** - Mapa colorido com caminho destacado
- [x] **Documentação** - Código comentado e README

### 🔧 Detalhes Técnicos
- **Linguagem**: Python 3.x
- **Bibliotecas**: NetworkX, Matplotlib
- **Heurística**: Distância euclidiana (admissível)
- **Complexidade**: O(b^d) onde b=ramificação, d=profundidade

---

## 📁 Estrutura do Projeto

```
algoritmodebusca/
├── profundidade.py    # Código principal (120 linhas)
└── README.md          # Esta documentação
```

---

## 🔬 Por que Funciona?

### Heurística Admissível
A distância euclidiana **nunca superestima** a distância real:
- Linha reta = menor distância possível entre 2 pontos
- Garante que A* encontre a solução ótima
- Mais eficiente que Dijkstra (explora menos nós)

### Algoritmo A* vs Outros
- **vs Dijkstra**: Mais rápido (usa heurística para direcionar busca)
- **vs BFS**: Considera pesos das arestas (mais preciso)
- **vs DFS**: Busca sistemática (não se perde em caminhos ruins)

---

## 🎓 Conceitos Demonstrados

1. **Modelagem de Problemas** - Transformar navegação real em grafo
2. **Busca Heurística** - A* com função de avaliação inteligente  
3. **Otimização** - Encontrar caminho mínimo eficientemente
4. **Visualização** - Apresentar resultados de forma clara
5. **Comparação Empírica** - Validar performance entre algoritmos

---



**Desenvolvido por**: Krislayne Vieira, Sara Ferreira e Pedro Gabriel | **Data**: Novembro 2025  
**Objetivo**: Demonstração didática do algoritmo A* aplicado à navegação urbana