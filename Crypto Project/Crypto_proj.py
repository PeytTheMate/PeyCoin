import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index      # Block number
        self.timestamp = time.time()    # Time block
        self.transactions = transactions  # List of transactions
        self.previous_hash = previous_hash  # Hash of previous block
        self.nonce = nonce      # Nonce used in mining 
        self.hash = self.calculate_hash()  # Current block hash


    def calculate_hash(self):

        block_content = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(block_content.encode()).hexdigest()
    


class Blockchain:
    def __init__(self):
        self.chain = [self.create.genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")
    
    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time.time()


# Proof of Work - This is where the "Crytpto Mining" happens

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4

    def mine_block(self, block):
        while block.hash[:self.difficulty] != "0" * self.difficulty:
            block.nonce += 1
            block.hash = block.calculate_hash()
        print(f"Congratulations! Block mined: {block.hash}")


# P2P (Peer to Peer) Networking

import socket
import threading

class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = []

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.host, self.port)
        server.listen(5)
        print(f"Node started on {self.host}:{self.port}")

        while True:
            client_socket, client_address = server.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()
    
    
    def handle_client(self, client_socket):
        pass


import ecdsa
import hashlib


class Wallet:
    def __init__(self):
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self,private_key = private_key.to_string().hex()
        self.public_key = private_key.get_verifying_key().to_string().hex()

    def sign_transaction(self, transaction):
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        message = str(transaction.sender) + str(transaction.receiever) + str(transaction.amount)
        signature = private_key.sign(message.encode())
        return signature.hex()
    
class Blockchain:
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            
            if current_block.hash != current_block.calculate_hash():
                return False
            
            if current_block.previous_has != previous_block.hash():
                return False
            
        return True
    

class Interface:
    def start(self):
        print("1. Check balance")
        print("2. Send cryptocurrency")
        print("3. Start mining")
        choice = input("Enter choice: ")

