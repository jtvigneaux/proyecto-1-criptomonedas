class Transaction:
    uniqueID = 0

    def __init__(self, value):
        self.type = "transaction"
        self.value = value
        self.uniqueID = Transaction.uniqueID
        Transaction.uniqueID += 1

    def __str__(self):
        string = "{{\n\t'type': {},\n\t'value': {},\n\t'uniqueID': {}\n}}".format(
            self.type, self.value, self.uniqueID)
        return string

    def __hash__(self):
        return self.uniqueID


if __name__ == "__main__":
    t = Transaction(50)
    t2 = Transaction(52)
    t3 = Transaction(54)
    print(t)
