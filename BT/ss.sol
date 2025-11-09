// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract student {

    struct Student {
        string name;
        uint256 rollno;
    }

    Student[] public studentarr;

    function addStudent(string memory name, uint rollno) public {
        for (uint i = 0; i < studentarr.length; i++) {
            if (studentarr[i].rollno == rollno) {
                revert("rollno already exists");
            }
        }
        studentarr.push(Student(name, rollno));
    }

    function getStudentsLength() public view returns (uint) {
        return studentarr.length;
    }

    function displayAllStudents() public view returns (Student[] memory) {
        return studentarr;
    }

    function getStudentsByIndex(uint idx) public view returns (Student memory) {
        require(idx < studentarr.length, "index out of range");
        return studentarr[idx];
    }

    fallback() external payable {}
    receive() external payable {}
}