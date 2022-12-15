USE  DDMRS;
CREATE TABLE Doctors (
Doctor_Id INT NOT NULL,
License_Number TEXT,
Doctor_Name VARCHAR(150) NOT NULL,
Hospital_Id INT NOT NULL,
Gender VARCHAR(20) NOT NULL,
PRIMARY KEY (Doctor_Id)
);
select * from Doctors;