SHOW DATABASES; #To view existing databases

USE DDMRS; 

CREATE TABLE Doctors (
    Doctor_Id INT NOT NULL,
    License_Number TEXT,
    Doctor_Name VARCHAR(150) NOT NULL,
    Degree TEXT,
    Practice_Specialities TEXT,
    Hospital_Id INT NOT NULL,
    Gender VARCHAR(20) NOT NULL,
    PRIMARY KEY (Doctor_Id)
    
);


SELECT * FROM Doctors;
