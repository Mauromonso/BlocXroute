from web3 import Web3
from collections import Counter

# === CONFIGURATION ===
INFURA_URL = 'https://mainnet.infura.io/v3/<YOUR_PROJECT_ID>'
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.is_connected():
    raise Exception("Web3 connection failed")

# === FETCH BLOCK DETAILS ===
BLOCK_NUMBER = 13507875
block = w3.eth.get_block(BLOCK_NUMBER, full_transactions=True)

# === INITIALIZE COUNTERS ===
from_addresses = []
to_addresses = []
highest_gas_tx = None
highest_gas_price = 0

# === ANALYZE TRANSACTIONS ===
for tx in block['transactions']:
    from_addresses.append(tx['from'])
    if tx['to']:
        to_addresses.append(tx['to'])

    gas_price = tx['gasPrice']
    if gas_price > highest_gas_price:
        highest_gas_price = gas_price
        highest_gas_tx = tx

# === FIND MOST COMMON ADDRESSES ===
most_common_sender = Counter(from_addresses).most_common(1)[0]
most_common_receiver = Counter(to_addresses).most_common(1)[0]

# === PRINT RESULTS ===
print(f"1) Sender with most transactions: {most_common_sender[0]} ({most_common_sender[1]} txns)")
print(f"2) Receiver with most transactions: {most_common_receiver[0]} ({most_common_receiver[1]} txns)")
print(f"3) Transaction with highest gas price:")
print(f"   - Hash: {highest_gas_tx['hash'].hex()}")
print(f"   - From: {highest_gas_tx['from']}")
print(f"   - To: {highest_gas_tx['to']}")
print(f"   - Gas Price: {w3.from_wei(highest_gas_tx['gasPrice'], 'gwei')} Gwei")
print(f"   - Value: {w3.from_wei(highest_gas_tx['value'], 'ether')} ETH")
