USE DDMRS; #using this database

CREATE TABLE Diseases (
    Disease_Id INT ,
    Disease_name VARCHAR(100) NOT NULL,
    Signs_and_symptoms TEXT,
    Diagnosis TEXT,
    Treatment TEXT,
    Disease_Category_Id INT,
    Doctor_Id INT,
    PRIMARY KEY (Disease_Id),
	FOREIGN KEY (Doctor_Id)
	REFERENCES Doctors (Doctor_Id)
    
);

SELECT * FROM Diseases;
update diseases set Doctor_Id=50 where Disease_Id= 12;

