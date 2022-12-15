USE  DDMRS;
CREATE TABLE DEGREE(
Doctor_Id INT NOT NULL,
Doctor_Degree TEXT,
FOREIGN KEY (Doctor_Id) References Doctors(Doctor_Id)
);
SELECT * FROM DEGREE;

