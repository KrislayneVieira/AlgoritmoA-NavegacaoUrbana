"""
Algoritmo A* - Navegação Urbana Simplificada
===========================================
Encontra o caminho mais curto entre dois pontos de uma cidade
Autores: Krislayne Vieira, Sara Ferreira e Pedro Gabriel  | Data: Novembro de 2025
"""

import networkx as nx
import matplotlib.pyplot as plt
import math


class BuscaAEstrela:
    def __init__(self):
        """Cria o grafo da cidade com coordenadas"""
        self.grafo = nx.Graph()
        self.coordenadas = {
            'Casa': (1, 1), 'Padaria': (2, 3), 'Mercado': (4, 2),
            'Escola': (6, 4), 'Hospital': (3, 6), 'Farmacia': (5, 5),
            'Banco': (7, 2), 'Centro': (5, 7), 'Parque': (8, 6)
        }
        self._criar_grafo()

    def _criar_grafo(self):
        """Cria o grafo com nós e arestas ponderadas"""
        # Adicionar nós
        for local, coord in self.coordenadas.items():
            self.grafo.add_node(local, pos=coord)

        # Conexões entre locais (ruas da cidade)
        conexoes = [
            ('Casa', 'Padaria'), ('Casa', 'Mercado'), ('Padaria', 'Hospital'),
            ('Mercado', 'Escola'), ('Mercado', 'Banco'), ('Escola', 'Farmacia'),
            ('Hospital', 'Centro'), ('Farmacia', 'Centro'), ('Farmacia', 'Parque'),
            ('Banco', 'Parque'), ('Centro', 'Parque')
        ]

        # Adicionar arestas com peso = distância euclidiana
        for local1, local2 in conexoes:
            peso = self._distancia(local1, local2)
            self.grafo.add_edge(local1, local2, weight=peso)

    def _distancia(self, local1, local2):
        """Calcula distância euclidiana entre dois locais"""
        x1, y1 = self.coordenadas[local1]
        x2, y2 = self.coordenadas[local2]
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def heuristica(self, atual, objetivo):
        """
        Heurística admissível: distância euclidiana
        (nunca superestima a distância real)
        """
        return self._distancia(atual, objetivo)

    def buscar_caminho(self, origem, destino):
        """Executa A* e retorna caminho + custo"""
        # A* usando NetworkX com nossa heurística
        caminho = nx.astar_path(self.grafo, origem, destino,
                                heuristic=self.heuristica, weight='weight')

        custo = nx.astar_path_length(self.grafo, origem, destino,
                                     heuristic=self.heuristica, weight='weight')

        return caminho, custo

    def comparar_algoritmos(self, origem, destino):
        """Compara A*, Dijkstra e BFS"""
        # A*
        caminho_astar, custo_astar = self.buscar_caminho(origem, destino)

        # Dijkstra (A* sem heurística)
        caminho_dijkstra = nx.shortest_path(
            self.grafo, origem, destino, weight='weight')
        custo_dijkstra = nx.shortest_path_length(
            self.grafo, origem, destino, weight='weight')

        # BFS (sem considerar pesos)
        caminho_bfs = nx.shortest_path(self.grafo, origem, destino)
        custo_bfs = sum(self.grafo[caminho_bfs[i]][caminho_bfs[i+1]]['weight']
                        for i in range(len(caminho_bfs)-1))

        return {
            'A*': {'caminho': caminho_astar, 'custo': custo_astar},
            'Dijkstra': {'caminho': caminho_dijkstra, 'custo': custo_dijkstra},
            'BFS': {'caminho': caminho_bfs, 'custo': custo_bfs}
        }

    def visualizar(self, origem, destino, caminho):
        """Desenha o mapa com o caminho encontrado"""
        plt.figure(figsize=(10, 8))

        # Todas as arestas em cinza
        nx.draw_networkx_edges(self.grafo, self.coordenadas,
                               edge_color='lightgray', width=1)

        # Caminho em vermelho
        arestas_caminho = [(caminho[i], caminho[i+1])
                           for i in range(len(caminho)-1)]
        nx.draw_networkx_edges(self.grafo, self.coordenadas,
                               edgelist=arestas_caminho, edge_color='red', width=3)

        # Cores dos nós
        cores = ['green' if no == origem else 'red' if no == destino
                 else 'yellow' if no in caminho else 'lightblue'
                 for no in self.grafo.nodes()]

        nx.draw_networkx_nodes(self.grafo, self.coordenadas,
                               node_color=cores, node_size=700)
        nx.draw_networkx_labels(self.grafo, self.coordenadas, font_size=9)

        # Pesos das arestas
        edge_labels = {k: f'{v:.1f}' for k, v in nx.get_edge_attributes(
            self.grafo, 'weight').items()}
        nx.draw_networkx_edge_labels(
            self.grafo, self.coordenadas, edge_labels, font_size=7)

        plt.title(f'A* - Caminho de {origem} para {destino}', fontsize=14)
        plt.grid(True, alpha=0.3)
        plt.show()

    def executar_demonstracao(self, origem='Casa', destino='Parque'):
        """Demonstração completa do A*"""
        print("=" * 50)
        print("🗺️  ALGORITMO A* - NAVEGAÇÃO URBANA")
        print("=" * 50)

        # Executar busca
        caminho, custo = self.buscar_caminho(origem, destino)

        print(f"🎯 Busca: {origem} → {destino}")
        print(f"📍 Caminho: {' → '.join(caminho)}")
        print(f"💰 Custo: {custo:.2f} unidades")
        print(f"🔢 Passos: {len(caminho)} nós")
        print(f"🧮 Heurística inicial: {self.heuristica(origem, destino):.2f}")

        print("\n📊 COMPARAÇÃO DE ALGORITMOS:")
        print("-" * 35)

        resultados = self.comparar_algoritmos(origem, destino)
        for alg, dados in resultados.items():
            print(
                f"{alg:>8}: Custo={dados['custo']:5.2f} | Nós={len(dados['caminho'])}")

        print(f"\n✅ Heurística Admissível: SIM")
        print(f"✅ Solução Ótima: GARANTIDA")

        # Mostrar visualização
        self.visualizar(origem, destino, caminho)


# EXECUÇÃO PRINCIPAL
if __name__ == "__main__":
    # Criar e executar busca A*
    busca = BuscaAEstrela()
    busca.executar_demonstracao('Casa', 'Parque')
