import hashlib
import time
class Block:
    def __init__(self,prev_hash,index,timestamp,data):
        self.data=data

        self.nonce=0

        self.prev_hash=prev_hash
        
        self.timestamp=timestamp
        
        self.index=index

        self.hash=self.calculate_hash()

    # to calculate hash 
    def calculate_hash(self):

        block_hash=str(self.index)+self.timestamp+self.data+self.prev_hash+str(self.nonce)
        
        return hashlib.sha256(block_hash.encode()).hexdigest()
        
    
    
    #PROOF - OF  - WORK (we will calculate the required nonce value such that the hash will start with number of zeroes specified)
    def mine_block(self,leading_zeroes):
        prefix='0'*leading_zeroes

        while not self.hash.startswith(prefix):
        
            self.nonce+=1
        
            # as nonce is changing we have to keep recomputing  the hash
        
            self.hash=self.calculate_hash()
        
        print(f"Block {self.index} mined: {self.hash}")
    

class Blockchain:
    def __init__(self):
        # initially chain will contain only Genesis Block 
        
        self.chain=[self.genesis_block()]
        
        self.leading_zeroes=2

    def genesis_block(self):
        
        zero_hash='0'*64  # for previous  hash
        Genesis_block=Block(zero_hash,0,time.ctime(),"Genesis Block")
        Genesis_block.mine_block(2)
        return Genesis_block
    
    def add_block(self,data):
        
        prev_block=self.chain[-1]
        
        # creating a new block 
        new_block=Block(prev_block.hash,len(self.chain),time.ctime(),data)

        # to generate hash of new block   and corresponding nonce value
        new_block.mine_block(self.leading_zeroes)
        
        self.chain.append(new_block)
    
    def is_valid(self):

        for i in range(1,len(self.chain)):
        
            current=self.chain[i]
        
            previous=self.chain[i-1]

            #checking if the current block hash is equal to the calculated hash
            if current.hash!=current.calculate_hash():
        
                print(f"Tampering detected at Block {i} ")
        
                return False   # returning false as chain is not valid
        
            if(current.prev_hash!=previous.hash):
                #link is broken between (i-1)  and (i)th  block
        
                print(f"Tampering detected between Block {i-1} and Block {i}")
        
                return False  # returning false as chain is not valid
        
        # if no issue found or chain is valid 
        return True


# testing 
Blockch=Blockchain()

Blockch.add_block("avinash")
Blockch.add_block("aditya")
Blockch.add_block("ayush")
Blockch.add_block("shiva")
Blockch.add_block("sachpreet")

for block in Blockch.chain:

    print(f"index: {block.index}\ntimestamp: {block.timestamp}\ndata: {block.data}\nNonce: {block.nonce}\nhash: {block.hash}\nprev_hash:  {block.prev_hash}\n")

print("Before Changes\n")
if Blockch.is_valid():

    print("Blockchain is valid \n")

# Changing data of third block 
Blockch.chain[3].data="ananya"

# To check if chain still valid
print("After  Changes\n")
if Blockch.is_valid():

    print("Blockchain is valid ")