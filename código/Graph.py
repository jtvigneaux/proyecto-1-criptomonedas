from collections import defaultdict
from random import random, randint

from Transaction import Transaction

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    _id = 0

    def __init__(self, malicious=0):
        self.id = Node._id
        Node._id += 1
        self.__transactions = set()
        self.__malicious = malicious

    def is_malicious(self):
        return bool(self.__malicious)

    def malicious_strategy(self):
        if self.__malicious == 3:
            return randint(1, 2)
        return self.__malicious

    def get_transactions(self):
        return self.__transactions

    def print_transactions(self):
        for transaction in self.get_transactions():
            print(transaction)

    def check_transaction(self, transaction):
        return transaction in self.get_transactions()

    def add_transaction(self, transaction):
        self.__transactions.add(transaction)

    def __hash__(self):
        return self.id


class Graph:

    def __init__(self):
        self.__nodes = []
        self.__connections = defaultdict(set)

        # Para mostrar el grafo
        self.display = nx.DiGraph()
        self.node_colors = {}
        self.malicious_nodes = 0

    def get_nodes(self):
        return self.__nodes

    def get_connections(self):
        return self.__connections

    def get_amount_of_nodes(self):
        return len(self.__nodes)

    def add_node(self, malicious=0):
        if malicious != 0:
            self.malicious_nodes += 1
        color = {0: 'grey'}
        new_node = Node(malicious=malicious)
        self.__nodes.append(new_node)
        # Grafico
        self.display.add_node(hash(new_node) + 1)
        self.node_colors[hash(new_node) + 1] = color.get(malicious, 'red')
        return new_node

    def add_connection(self, a, b):
        if a in self.get_nodes() and b in self.get_nodes():
            self.get_connections()[a].add(b)
            self.display.add_edge(hash(a) + 1, hash(b) + 1)

    def __repr__(self):
        repr_str = ''
        for node in self.get_nodes():
            repr_str += '{} - {}\n'.format(hash(node),
                                           self.get_connections()[node])
        return repr_str

    def propagate_message(self, node, transaction, first=True):
        if node.check_transaction(transaction) or \
                node.malicious_strategy() == 1 or \
                (node.malicious_strategy() == 2 and not first):
            return
        node.add_transaction(transaction)
        for n in self.__connections[node]:
            self.propagate_message(n, transaction, first=False)

    def show_graph(self):
        # Need to create a layout when doing
        # separate calls to draw nodes and edges
        pos = nx.spring_layout(self.display)
        nx.draw_networkx_nodes(
            self.display, pos, cmap=plt.get_cmap('jet'), node_color=list(self.node_colors.values()), node_size=500)
        nx.draw_networkx_labels(self.display, pos)
        nx.draw_networkx_edges(
            self.display, pos, edgelist=self.display.edges(), arrows=True)
        plt.show()


def GenNetwork(n, p, ppp=0.1):
    graph = Graph()
    connections = []
    for i in range(n):
        graph.add_node(0 if random() > ppp else randint(1, 3))
        for j in range(n):
            if random() < p:
                connections.append((i, j))
    for connection in connections:
        i, j = connection
        a, b = graph.get_nodes()[i], graph.get_nodes()[j]
        graph.add_connection(a, b)
    return graph

if __name__ == '__main__':

    #g = Graph()
    #a = g.add_node()
    #b = g.add_node()
    #c = g.add_node()
    #g.add_connection(a, b)
    #g.add_connection(a, c)
    #g.add_connection(c, a)
    #g.propagate_message(a, Transaction(10))
    #print(a.get_transactions(), b.get_transactions(), c.get_transactions())
    # print(g)
    g = GenNetwork(10, 0.60)
    g.show_graph()
