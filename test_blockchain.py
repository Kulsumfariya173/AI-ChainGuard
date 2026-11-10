from blockchain import Blockchain

my_chain = Blockchain()

my_chain.add_block({
    "event": "Multiple failed login attempts",
    "status": "Suspicious",
    "risk": "High"
})

my_chain.add_block({
    "event": "Unauthorized access attempt",
    "status": "Threat Detected",
    "risk": "Critical"
})

print("\n========== BLOCKCHAIN DETAILS ==========")

for block in my_chain.chain:

    print("\nBlock:", block.index)
    print("Data:", block.data)
    print("Hash:", block.hash)
    print("Previous Hash:", block.previous_hash)

print("\nBlockchain Valid:", my_chain.is_chain_valid())
print("\n========== BLOCKCHAIN TAMPERING TEST ==========")

# Modify an existing block's data
my_chain.chain[1].data = {
    "event": "Modified Unauthorized Activity",
    "status": "Normal",
    "risk": "Low"
}

# Verify blockchain integrity
print("Blockchain Valid After Tampering:", my_chain.is_chain_valid())