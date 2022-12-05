# Disease Diagnosis and Medic Recommendation System


**Data Set Sources:**

The data for the database will be scraped from multiple websites like Wikipedia, massgov and zocdoc
1.	https://en.wikipedia.org/wiki/List_of_infectious_diseases  -- used in "Diseases.py" file.
2.	https://findmydoctor.mass.gov/-  -- used in  "DbConnection.py" file.
3.	https://book.zocdoc.com/get-started?utm_source=google&utm_medium=cpc_brand&utm_campaign=12793676051&utm_term=zocdoc&utm_content=122847269722&gclid=Cj0KCQiAyracBhDoARIsACGFcS4A6qzB0YXJxWA38QHgLCAzyguZ21J5V2UENmSYWg7mZ8exMcZavekaAoCcEALw_wcB  -- used in "main.py" file.
4.	https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=540  -- used in "main.py" file.




****Python Scripts:****

1.	Using Beautiful Soup library (bs4) in python we scrape the necessary data required from the sources stated above and store them in CSV Files.
2.	Later these CSV files are cleaned to exclude duplicate values, null values and special characters using cleaning scripts (displayed in Py files).
3.	The cleaned data is inserted into SQL tables which will populate the following tables:
  -  Diseases
  -  Doctors
  -  Hospitals
  -  Disease Categories
4.	Please refer to the SQL Scripts folder for the physical model.


**Audit Data/Data Visualization:**

1. As part of Data Auditing, that data that is collected is Visualized using Seaborn library showing the statistics of data collected  -- shown in "Visualization Scripts.ipynb" file.




**Physical Model (SQL):**

The physical model for our database is present in the "SQL Scripts" folder.

1. The "Diseases Table.sql" file has the schema for the Diseases table consisting of all infectious diseases.
2. The "Diseases Categories table.sql" file has the schema for the Diseases Categories for the infectious diseases.
3. The "Doctors table.sql" file has the schema for the doctors data.
4. The "Hospitals table.sql" file has the schema for the hospitals data.




**Results:**

1. The resulant screenshots of data inserted into the Diseases table is present in the Disease-Diagnosis-and-Medic-Recommendation-System/Assignment_3_DMDD_Data_Sherpas/Results/Diseases.png

2. The resultant screenshots of data inserted into the Disease Categories table is present in the Disease-Diagnosis-and-Medic-Recommendation-System/Assignment_3_DMDD_Data_Sherpas/Results/DiseaseCategories.png

3. The resultant screenshots of data inserted into the Doctors table is present in the Disease-Diagnosis-and-Medic-Recommendation-System/Assignment_3_DMDD_Data_Sherpas/Results/Doctors.png

4. The resultant screenshots of data inserted into the Hospitals table is present in the Disease-Diagnosis-and-Medic-Recommendation-System/Assignment_3_DMDD_Data_Sherpas/Results/Hospitals.png






# CONTRIBUTORS

1. Rohit Panicker | NUID: 002791446
2. Rohit Paul | NUID: 002908933 
3. Akshatha Patil | NUID: 002657158
