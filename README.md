# Home Assignment - Technical Support Manager @Bloxroute

## By Mauro Monso

### Introduction
This `README.md` document is part of the home assignment for the Technical Support Manager role at BloXroute. The objective is to demonstrate problem-solving abilities, blockchain knowledge, and scripting skills using tools like [Etherscan](https://etherscan.io/), [Infura](https://infura.io/), and web3 libraries. The assignment is structured into three exercises:

- **Exercise 1:** Ethereum transaction inspection and scripting with Etherscan and web3 libraries.
- **Exercise 2:** Troubleshooting blockchain-related issues on Ethereum and Solana networks.
- **Exercise 3 (Optional):** Smart contract development to track and manage ETH and ERC20 tokens.

This document provides a detailed 1-to-1 mapping of the assignment questions, requirements, and solutions in a GitHub-compatible markdown format.

---

## Exercise 1
For this exercise, please use [Etherscan](https://etherscan.io/) for inspection at first and then write scripts to query data.

### Etherscan Inspection
Using Etherscan, find block `13507871` and provide the following information:

1. **Who mined the block?**
2. **How many transactions does it contain?**
3. **Which transaction is sent by `Coinbase 1` account** (`0x71660c4005ba85c37ccec55d0c4493e66fe775d3`)?

### Script 1
Focus on the transaction sent by `Coinbase 1` account. Write a script to use the endpoint to get the following information about this transaction:
- To address
- Gas price
- Input call data

Additionally:
- Assume you are the owner of `Coinbase 1` and construct input call data to transfer 100 USDC tokens to `Binance 10` account (`0x85b931A32a0725Be14285B66f1a22178c672d69B`).

### Etherscan Inspection
After block `13507871`, identify the next block (block height `h`) mined by the same miner.

### Script 2
Query the block at height `h` to get the following information:
1. Sender (from address) that sent most transactions in this block
2. Receiver (to address) that received most transactions in this block
3. Transaction with the highest gas price

---

## Exercise 2

1. **Ethereum Transaction Issue:**
   - A customer reports that their Ethereum transaction is missing on Etherscan. How would you troubleshoot this issue? How would the process differ on the Solana network?

2. **API Error Troubleshooting:**
   - An inexperienced programmer receives a “AxiosError: Request failed with status code 500” in their JavaScript code. How would you help them troubleshoot the problem?

3. **Docker Compatibility Issue:**
   - A programmer tries to run Solana's Docker image on the latest Apple MacBook with M4 Chip and faces issues. What potential error/warning messages might appear and why?

4. **Blockchain Validator Behavior:**
   - A validator duplicates the same transaction multiple times in a block to receive the same transfer multiple times. What would happen to the transactions and the block?

5. **Token Recovery Scenario:**
   - If 100 USDT tokens are mistakenly sent to a zero address on Ethereum, could you recover them by controlling all Ethereum validators or by being the owner of Tether? How?

---

## Exercise 3 [Optional]

Create a smart contract that:
1. Tracks and displays the amount of ETH and any ERC20 token this contract holds.
2. Allows any sender to send ETH to this contract.
3. Allows the contract owner to withdraw all available ETH stored in this contract.
4. Allows non-owner wallets to withdraw 10% of the ETH stored in this contract.

If deployed to a testnet, provide the verification details on Etherscan.

---

This `README.md` provides a detailed mapping of the home assignment questions and requirements for the Technical Support Manager role at BloXroute, formatted for easy navigation on GitHub.
