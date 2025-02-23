from web3 import Web3

# === CONFIGURATION ===
INFURA_URL = 'https://mainnet.infura.io/v3/<YOUR_PROJECT_ID>'
TRANSACTION_HASH = '0x2ad2bb00718ab0ed8310dacff9c029ea5d41e038d96c9f52561a1e7948759e99' # Tx Hash for the transaction sent by Coinbase 1

# === INITIALIZE WEB3 ===
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not w3.is_connected():
    raise Exception("Web3 connection failed")

# === FETCH TRANSACTION DETAILS ===
tx = w3.eth.get_transaction(TRANSACTION_HASH)

print(f"1) To Address: {tx['to']}")
print(f"2) Gas Price: {w3.from_wei(tx['gasPrice'], 'gwei')} Gwei")

# === Decode Input Call Data ===
input_data = tx['input']

# Convert HexBytes to hex string if necessary
if isinstance(input_data, bytes):
    input_data = input_data.hex()

# Ensure the input data is a hex string without '0x' prefix
if input_data.startswith('0x'):
    input_data = input_data[2:]

# Extract correct function selector (first 8 hex chars)
function_selector = input_data[:8]

# Parameters follow the function selector
params = input_data[8:]

# Extract recipient (next 32 bytes)
recipient_hex = params[24:64]  # Skip the left padding (12 bytes of zeros)
recipient = Web3.to_checksum_address('0x' + recipient_hex)

# Extract amount (next 32 bytes)
amount_hex = params[64:128]
amount = int(amount_hex, 16) / 10**6  # USDC uses 6 decimals

# === Display the decoded data ===
print(f"3) Input Call Data:")
print(f"   - Function Selector: 0x{function_selector}")
print(f"   - Recipient: {recipient}")
print(f"   - Amount: {amount} USDC")
