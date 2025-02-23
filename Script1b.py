from web3 import Web3


# === CONFIGURATION ===
INFURA_URL = 'https://mainnet.infura.io/v3/YOUR_PROJECT_ID'
w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# USDC Contract Address (or any ERC-20)
TOKEN_CONTRACT_ADDRESS = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48'  # USDC on Ethereum Mainnet

# Recipient and Amount (as per input call data)
recipient = '0x85b931A32a0725Be14285B66f1a22178c672d69B'  # BINANCE 10 ADDRESS
amount = 100000000  # 100 USDC (considering 6 decimals)

# === ENCODE FUNCTION CALL ===
function_selector = w3.keccak(text="transfer(address,uint256)")[:4]
recipient_padded = w3.to_bytes(hexstr=recipient[2:]).rjust(32, b'\x00')
amount_padded = w3.to_bytes(amount).rjust(32, b'\x00')
input_call_data = w3.to_hex(function_selector + recipient_padded + amount_padded)

print("Encoded Transfer Call Data:")
print(f"   - Function Selector: {function_selector.hex()}")
print(f"   - Recipient: {recipient}")
print(f"   - Amount: {amount / 10**6} USDC")
print(f"   - Input Call Data: {input_call_data}")

