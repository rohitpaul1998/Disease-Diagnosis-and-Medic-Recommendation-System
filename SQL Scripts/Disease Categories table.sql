SHOW DATABASES; #To view existing databases

USE DDMRS; 

CREATE TABLE DiseaseCategory (
    Disease_Category_Id INT NOT NULL,
    Disease_Category_Name VARCHAR(150) NOT NULL UNIQUE,
    PRIMARY KEY (Disease_Category_Id)
   );

select * from DiseaseCategory;