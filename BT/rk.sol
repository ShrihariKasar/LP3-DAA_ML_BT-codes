// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {

    address public accOwner;

    constructor() {
        accOwner = msg.sender;
    }

    // Deposit money into the contract
    function deposit() public payable {
        require(msg.sender == accOwner, "You are not the account owner");
        require(msg.value > 0, "Deposit must be greater than zero");
        // Money automatically gets added to contract balance
    }

    // Withdraw money from the contract
    function withdraw(uint amount) public {
        require(msg.sender == accOwner, "You are not the account owner");
        require(amount > 0, "Withdraw amount must be more than zero");
        require(amount <= address(this).balance, "Not enough balance in contract");

        payable(accOwner).transfer(amount);
    }

    // Show real Ether balance inside contract
    function showBalance() public view returns (uint256) {
        require(msg.sender == accOwner, "You are not the account owner");
        return address(this).balance;
    }
}