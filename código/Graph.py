from collections import defaultdict
from random import randint


class Node:
    _id = 0

    def __init__(self, malicius=False, transactions=set()):
        self.id = Node._id
        Node._id += 1
        self.__transactions = transactions
        self.__malicius = malicius

    def is_malicius(self):
        return self.malicius

    def get_transactions(self):
        return self.__transactions

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

    def add_node(self):
        new_node = Node()
        self.__nodes.append(new_node)

    def add_connection(self, a, b):
        if a in self.get_nodes() and b in self.get_nodes():
            self.get_connections()[a].add(b)


if __name__ == '__main__':

    g = Graph()
