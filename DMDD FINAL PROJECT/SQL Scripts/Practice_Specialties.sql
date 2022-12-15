USE  DDMRS;
CREATE TABLE Practice_Specialities (
Doctor_Id INT NOT NULL,
Practice_Specialities VARCHAR(300),
PRIMARY KEY (Doctor_Id,Practice_Specialities),
FOREIGN KEY (Doctor_Id) REFERENCES Doctors(Doctor_Id));

select * from Practice_Specialities;