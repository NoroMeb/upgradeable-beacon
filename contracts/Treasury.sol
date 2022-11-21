// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import "@openzeppelin/contracts/proxy/utils/Initializable.sol";

contract Treasury is Initializable {
    uint256 public value;

    function initialize(uint256 _value) external initializer {
        value = _value;
    }

    function increment() external {
        value++;
    }
}
