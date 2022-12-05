SHOW DATABASES; #To view existing databases

USE DDMRS; 
CREATE TABLE Hospitals (
    Hospital_Id INT NOT NULL,
    Hospital_Affliations TEXT,
    City VARCHAR(150) NOT NULL,
    State VARCHAR(20),
    Zip_Code BIGINT NOT NULL,
    PRIMARY KEY (Zip_Code),
    FOREIGN KEY (Hospital_Id)
        REFERENCES Doctors (Doctor_Id)
);



SELECT * FROM Hospitals;
