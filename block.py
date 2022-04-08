import hashlib

class NeuralCoinBlock:
    def __init__(self, previous_block_hash , transaction_list):
        self.previous_block_hash = previous_block_hash 
        self.transaction_list = transaction_list
        self.block_data = "-".join(transaction_list)  + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Mary sends 2 NuralCoin to jenny"
t2 = "mike sends 1.6 NuralCoin to james"
t3 = "bob sends 1.5 NuralCoin to bobby"
t4 = "Mary sends 4 NuralCoin to zimmy"
t5 = "Mary sends 2.5 NuralCoin to henry"

initial_block = NerualCoinBlock("Initial String ",[t1,t2])

print(initial_block.block_data)