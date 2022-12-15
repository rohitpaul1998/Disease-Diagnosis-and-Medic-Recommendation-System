USE  DDMRS;
CREATE TABLE PINCODES_STATE_CITY(
City VARCHAR(150) NOT NULL,
State VARCHAR(20),
Zip_Code INT NOT NULL,
Hospital_Id INT NOT NULL,
PRIMARY KEY (Hospital_Id),
FOREIGN KEY (Hospital_Id)
References Hospitals(Hospital_Id)
);
select * from PINCODES_STATE_CITY;