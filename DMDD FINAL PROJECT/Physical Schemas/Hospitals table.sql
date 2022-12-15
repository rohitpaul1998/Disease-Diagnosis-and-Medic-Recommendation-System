USE  DDMRS;
CREATE TABLE Hospitals (
Hospital_Id INT NOT NULL,
Zip_Code BIGINT NOT NULL,
PRIMARY KEY (Hospital_Id),
FOREIGN KEY (Hospital_Id)
REFERENCES Doctors (Doctor_Id)
);
select * from Hospitals;