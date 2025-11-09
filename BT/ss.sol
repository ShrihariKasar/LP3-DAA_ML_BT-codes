//Student Details

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.30;

contract StudentMarks {
    // Structure to store student details
    struct Student {
        uint256 stud_id;
        string name;
        uint256 marks;
    }

    // Array to store multiple students
    Student[] private students;

    // Function to add a new student
    function addStudent(uint256 stud_id, string memory name, uint256 marks) public {
        require(marks <= 100, "Marks must be between 0 and 100");
        students.push(Student(stud_id, name, marks));
    }

    // Function to calculate and return average marks
    function getAverageMarks() public view returns (uint256) {
        require(students.length > 0, "No students found");
        uint256 total = 0;

        for (uint256 i = 0; i < students.length; i++) {
            total += students[i].marks;
        }

        return total / students.length;
    }
}
