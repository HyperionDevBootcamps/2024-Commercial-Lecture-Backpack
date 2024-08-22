-- •	Creating a Database: 
-- o	    Show how to create a new database.
-- o        Create a file that will be the database

-- •	Creating Tables: 
-- o	    Demonstrate creating a table with primary and foreign keys.

CREATE TABLE Students (
    StudentID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER
);

CREATE TABLE Courses (
    CourseID INTEGER PRIMARY KEY,
    CourseName TEXT
);

CREATE TABLE Enrollments (
    EnrollmentID INTEGER PRIMARY KEY,
    StudentID INTEGER,
    CourseID INTEGER,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (CourseID) REFERENCES Courses(CourseID)
);

-- •	Inserting Data: 
-- o	    Show how to insert data into tables.

INSERT INTO Students (Name, Age) VALUES ('Julien', 20);
INSERT INTO Students (Name, Age) VALUES ('Marc', 50);

INSERT INTO Courses (CourseName) VALUES ('Software Engineering');
INSERT INTO Courses (CourseName) VALUES ('Data Science');

INSERT INTO Enrollments (StudentID, CourseID) VALUES (1, 1);
INSERT INTO Enrollments (StudentID, CourseID) VALUES (1, 2);
INSERT INTO Enrollments (StudentID, CourseID) VALUES (2, 2);

-- •	Querying Data with Joins: 
-- o	    Demonstrate basic SELECT queries with joins.

SELECT * FROM Students;
SELECT * FROM Courses;
SELECT * FROM Enrollments;

-- Inner Join
SELECT Students.Name, Courses.CourseName
FROM Enrollments
JOIN Students ON Enrollments.StudentID = Students.StudentID
JOIN Courses ON Enrollments.CourseID = Courses.CourseID;

-- Left Join
SELECT Students.Name, Courses.CourseName
FROM Students
LEFT JOIN Enrollments ON Students.StudentID = Enrollments.StudentID
LEFT JOIN Courses ON Enrollments.CourseID = Courses.CourseID;

-- •	Updating and Deleting Data: 
-- o	    Show how to update and delete records.
UPDATE Students SET Age = 22 WHERE StudentID = 1;
DELETE FROM Students WHERE StudentID = 1;
