USE  DDMRS;

CREATE TABLE Hospital_Affiliations(
Hospital_Id INT NOT NULL,
Hospital_Affliations VARCHAR(300),
PRIMARY KEY (Hospital_Id,Hospital_Affliations),
FOREIGN KEY (Hospital_Id)
       REFERENCES Hospitals (Hospital_Id)
);
select * from Hospital_Affiliations;