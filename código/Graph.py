from collections import defaultdict
from random import random, randint

from Transaction import Transaction


class Node:
    _id = 0

    def __init__(self, malicious=0, transactions=set()):
        self.id = Node._id
        Node._id += 1
        self.__transactions = transactions
        self.__malicious = malicious

    def is_malicious(self):
        return bool(self.__malicious)

    def malicious_strategy(self):
        if self.__malicious == 3:
            return randint(1, 2)
        return self.__malicious

    def get_transactions(self):
        return self.__transactions

    def check_transaction(self, transaction):
        return transaction in self.get_transactions()

    def add_transaction(self, transaction):
        self.__transactions.add(transaction)

    def __hash__(self):
        return self.id


class Graph:

    def __init__(self, nodes=[]):
        self.__nodes = nodes
        self.__connections = defaultdict(set)

    def get_nodes(self):
        return self.__nodes

    def get_connections(self):
        return self.__connections

    def add_node(self, malicious=0):
        new_node = Node(malicious=malicious)
        self.__nodes.append(new_node)
        return new_node

    def add_connection(self, a, b):
        if a in self.get_nodes() and b in self.get_nodes():
            self.get_connections()[a].add(b)

    def __repr__(self):
        repr_str = ''
        for node in self.get_nodes():
            repr_str += '{} - {}\n'.format(hash(node),
                                           self.get_connections()[node])
        return repr_str

    def propagate_message(self, node, transaction, first=True):
        if node.check_transaction(transaction) or \
                node.malicious_strategy() == 1 or \
                (self.malicious_strategy() == 2 and not first):
            return
        node.add_transaction(transaction)
        for n in self.get_connections()[node]:
            self.propagate_message(n, transaction, first=False)


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
    g = GenNetwork(10, 0.4)
