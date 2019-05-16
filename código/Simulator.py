import random
from Graph import Graph
from Transaction import Transaction


class Simulator:
	def __init__(self, graph, p, pp, ppp, k):
		self.graph = graph
		self.prob_connectivity = p  # Probability between 0 and 1
		self.prob_receive_message = pp
		self.prob_malicious = ppp
		self.rounds = k  # Number of rounds 

	def generate_transactions(self):
		transactions = [Transaction(random.randint(1, 50)) for i in range(10)]
		return transactions

	def run(self):
		# 1 ronda
		transactions = self.generate_transactions()
		for transaction in transactions:
			for node in self.graph.get_nodes():
				if random.random() < self.prob_receive_message:
					self.graph.propagate_message(node, transaction)	
			
		
		for node in self.graph.get_nodes():
			print("NODO {}".format(node.id))
			node.print_transactions()




if __name__ == "__main__":
	graph = Graph()
	n1 = graph.add_node()
	n2 = graph.add_node()
	n3 = graph.add_node()
	n4 = graph.add_node()
	n5 = graph.add_node()
	n6 = graph.add_node()
	simulator = Simulator(graph, 0.4, 0.5, 0.1, 1)

	simulator.run()
