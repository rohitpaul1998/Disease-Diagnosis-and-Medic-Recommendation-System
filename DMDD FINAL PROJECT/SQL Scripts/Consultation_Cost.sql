USE  DDMRS;

CREATE TABLE Consultation_Cost(
Id INT NOT NULL,
Cost  INT NOT NULL,
Hospital_Id INT NOT NULL,
Doctor_Id INT NOT NULL,
PRIMARY KEY (Id),
FOREIGN KEY (Doctor_Id)
	REFERENCES Doctors (Doctor_Id),
    FOREIGN KEY (Hospital_Id)
	REFERENCES Hospitals(Hospital_Id)
);
Select*from Consultation_Cost;
