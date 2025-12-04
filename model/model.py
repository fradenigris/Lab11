import networkx as nx
from database.dao import DAO


class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._nodes = None
        self._edges = None

    def build_graph(self, year: int):
        """
        Costruisce il grafo (self.G) dei rifugi considerando solo le connessioni
        con campo `anno` <= year passato come argomento.
        Quindi il grafo avrà solo i nodi che appartengono almeno ad una connessione, non tutti quelli disponibili.
        :param year: anno limite fino al quale selezionare le connessioni da includere.
        """
        # TODO

        self.G.clear()

        self._edges = DAO.get_connessioni_filtrate(year)
        all_rifugi = DAO.get_all_rifugi()
        insieme = set()
        self._nodes = set()

        for conn in self._edges:
            for rif in all_rifugi:
                if rif.id == conn.id_rifugio1 or rif.id == conn.id_rifugio2:
                    insieme.add(rif.id)

        for rif in all_rifugi:
            if rif.id in insieme:
                self._nodes.add(rif)

        self.G.add_nodes_from(self._nodes)

        for conn in self._edges:
            for rif1 in all_rifugi:
                for rif2 in all_rifugi:
                    if rif1.id != rif2.id:
                        if ((rif1.id == conn.id_rifugio1 and rif2.id == conn.id_rifugio2)
                                or (rif1.id == conn.id_rifugio2 and rif2.id == conn.id_rifugio1)):

                            self.G.add_edge(rif1, rif2)
                            conn.id_rifugi.add(rif1)
                            conn.id_rifugi.add(rif2)


    def get_nodes(self):
        """
        Restituisce la lista dei rifugi presenti nel grafo.
        :return: lista dei rifugi presenti nel grafo.
        """
        # TODO

        return self._nodes

    def get_num_neighbors(self, node):
        """
        Restituisce il grado (numero di vicini diretti) del nodo rifugio.
        :param node: un rifugio (cioè un nodo del grafo)
        :return: numero di vicini diretti del nodo indicato
        """
        # TODO

        # METODO ITERATIVO
        """
        count = 0
        for conn in self._edges:
            if node.id == conn.id_rifugio1 or node.id == conn.id_rifugio2:
                count += 1
        return count
        """

        # FUNZIONE DI NETWORKX
        lista_vicini = list(self.G.neighbors(node))
        return len(lista_vicini)

    def get_num_connected_components(self):
        """
        Restituisce il numero di componenti connesse del grafo.
        :return: numero di componenti connesse
        """
        # TODO

        return nx.number_connected_components(self.G)

    def get_reachable(self, start):
        """
        Deve eseguire almeno 2 delle 3 tecniche indicate nella traccia:
        * Metodi NetworkX: `dfs_tree()`, `bfs_tree()`
        * Algoritmo ricorsivo DFS
        * Algoritmo iterativo
        per ottenere l'elenco di rifugi raggiungibili da `start` e deve restituire uno degli elenchi calcolati.
        :param start: nodo di partenza, da non considerare nell'elenco da restituire.

        ESEMPIO
        a = self.get_reachable_bfs_tree(start)
        b = self.get_reachable_iterative(start)
        b = self.get_reachable_recursive(start)

        return a
        """

        # TODO

        # PRIMO METODO (dfs_tree())
        """
        dfs = nx.dfs_tree(self.G, source = start)
        if dfs.has_node(start):
            dfs.remove_node(start)

        return dfs.nodes()
        """

        # SECONDO METODO
        visitati = []
        da_visitare = [start]

        while len(da_visitare) > 0:
            current_node = da_visitare.pop()

            if current_node not in visitati:
                visitati.append(current_node)

                vicini = self.G.neighbors(current_node)
                da_visitare.extend(vicini)

        visitati.remove(start)
        return list(visitati)
