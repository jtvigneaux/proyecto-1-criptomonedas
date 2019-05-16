import random
from Transaction import Transaction


class Simulator:
	def __init__(self, graph, p, k):
		self.graph = graph
		self.p = p  # Probability
		self.rounds = k  # Number of rounds 

	def generate_transactions(self):
		transactions = [Transaction(random.randint(1, 50)) for i in range(10)]
		return transactions

	def run(self):
		trans = self.generate_transactions()
		for t in trans:
			print(t)


if __name__ == "__main__":
	simulator = Simulator(None, 0.6, 1)
	simulator.run()
