import random
from Graph import Graph, GenNetwork
from Transaction import Transaction
from collections import defaultdict


class Simulator:
	def __init__(self, graph, p, pp, ppp, k):
		self.graph = graph
		self.prob_connectivity = p  # Probability between 0 and 1
		self.prob_receive_message = pp
		self.prob_malicious = ppp
		self.rounds = k  # Number of rounds
		self.consensus = []

	def generate_transactions(self):
		transactions = [Transaction(random.randint(1, 50)) for i in range(10)]
		return transactions

	def nodes_in_consensus(self):
		#sets_of_transactions = defaultdict(0)
		sets_of_transactions = []
		number_of_nodes = []
		for node in self.graph.get_nodes():
			if node.get_transactions() not in sets_of_transactions:
				sets_of_transactions.append(node.get_transactions())
				number_of_nodes.append(1)
			else:
				index = sets_of_transactions.index(node.get_transactions())
				number_of_nodes[index] += 1
		consensus = max(number_of_nodes)
		self.consensus.append(consensus)
		return consensus

	def print_nodes_info(self):
		for node in self.graph.get_nodes():
			print("NODO {}".format(node.id))
			node.print_transactions()

	def statistics(self):
		pass
			
	def run(self):
		
		for round in range(self.rounds):
			# 1 ronda	
			transactions = self.generate_transactions()
			for transaction in transactions:
				for node in self.graph.get_nodes():
					if random.random() < self.prob_receive_message:
						# print("Nodo {} recibe mensaje {} para propagar".format(node.id, transaction.uniqueID))
						self.graph.propagate_message(node, transaction)	
				
			# self.print_nodes_info()	
			print("RONDA {} | Máximo número de nodos en consenso: {}".format(round + 1, self.nodes_in_consensus()))




if __name__ == "__main__":
	graph = Graph()
	n1 = graph.add_node()
	n2 = graph.add_node()
	n3 = graph.add_node()
	n4 = graph.add_node()
	n5 = graph.add_node()
	n6 = graph.add_node(1)
	graph.add_connection(n1, n2)
	graph.add_connection(n2, n3)
	graph.add_connection(n3, n4)
	graph.add_connection(n4, n5)
	graph.add_connection(n5, n6)
	graph.add_connection(n6, n1)
	#simulator = Simulator(graph, 0.4, 0.5, 0.1, 10)
	random_graph = GenNetwork(6, 0.4, 0.1)
	simulator = Simulator(random_graph, 0.4, 0.5, 0.1, 10)

	simulator.run()
	
