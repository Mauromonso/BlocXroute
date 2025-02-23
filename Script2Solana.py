import requests
import json

SOLANA_RPC_URL = 'https://api.mainnet-beta.solana.com'
tx_signature = 'YOUR_TRANSACTION_SIGNATURE_HERE'  # Replace with customer's signature
                                                  #'5dUH5AsJwyGY56RrmFqoNqS2j3aNhQMPqDLbKebmHwvF5pCECc39ycAP6274yuLBaHfKSutAJKnrE9fP5A8ty5bp' example signature

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "getTransaction",  
    "params": [
        tx_signature,
        {
            "encoding": "json",
            "maxSupportedTransactionVersion": 0  
        }
    ]
}

response = requests.post(SOLANA_RPC_URL, json=payload)

try:
    data = response.json()

    # Handle RPC errors
    if 'error' in data:
        print("RPC Error:", data['error']['message'])
    elif data.get('result'):
        print("Transaction Found:", json.dumps(data['result'], indent=2))
    else:
        print("Transaction Not Found")
except json.JSONDecodeError:
    print("Failed to parse JSON response.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
