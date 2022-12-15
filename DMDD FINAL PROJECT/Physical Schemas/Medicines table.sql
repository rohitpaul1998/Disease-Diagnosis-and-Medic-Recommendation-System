show schemas;

use ddmrs;

CREATE TABLE Medicines (
    ID INT NOT NULL,
    Drug_Name VARCHAR(200) NOT NULL,
    Manufacturer_Name TEXT,
    Price DECIMAL(10 , 2 ) NOT NULL,
    Disease_Category_Id INT NOT NULL,
    FOREIGN KEY (Disease_Category_Id)
        REFERENCES DiseaseCategory (Disease_Category_Id)
);

SELECT * FROM Medicines;