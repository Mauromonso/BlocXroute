from web3 import Web3

# Connect to Infura node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/<YOUR_PROJECT_ID>'))

# Customer’s transaction hash
customer_tx_hash = '<YOUR_TX_HASH>'

# Fetch transaction details
try:
    tx = w3.eth.get_transaction(customer_tx_hash)
    receipt = w3.eth.get_transaction_receipt(customer_tx_hash)

    if receipt is None:
        print("Transaction is still pending.")
    else:
        print("Transaction has been mined.")
        print(f"Block Number: {receipt.blockNumber}")
        print(f"Gas Used: {receipt.gasUsed}")
except Exception as e:
    if "not found" in str(e):
        print("Transaction not found. It might not have been broadcasted properly.")
    else:
        print(f"An error occurred: {e}")
