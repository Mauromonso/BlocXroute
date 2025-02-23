// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}

contract OptionalEthAndTokenTracker {
    address public owner;
    mapping(address => bool) public hasWithdrawn;
    uint256 public totalWithdrawals;

    constructor() {
        owner = msg.sender;
    }

    // Fallback and Receive Functions to accept ETH
    receive() external payable {}
    fallback() external payable {}

    // Function to get the ETH balance of this contract
    function getEthBalance() public view returns (uint256) {
        return address(this).balance;
    }

    // Function to get the ERC20 token balance of this contract
    function getTokenBalance(address tokenAddress) public view returns (uint256) {
        return IERC20(tokenAddress).balanceOf(address(this));
    }

    // Function to withdraw all ETH (Owner only)
    function withdrawAllEth() public {
        require(msg.sender == owner, "Only owner can withdraw all ETH");
        uint256 amount = address(this).balance;
        payable(owner).transfer(amount);
    }

    // Function for non-owners to withdraw 10% of the ETH balance
    function withdrawTenPercent() public {
        require(msg.sender != owner, "Owner cannot withdraw 10%");
        require(!hasWithdrawn[msg.sender], "You have already withdrawn your 10%");
        uint256 tenPercent = address(this).balance / 10;
        require(tenPercent > 0, "Insufficient balance to withdraw 10%");

        hasWithdrawn[msg.sender] = true;
        totalWithdrawals += tenPercent;
        payable(msg.sender).transfer(tenPercent);
    }
}
