# Disease Diagnosis and Medic Recommendation System

Data Set Sources:

The data for the database will be scraped from multiple websites like Wikipedia, massgov and zocdoc
1.	https://en.wikipedia.org/wiki/List_of_infectious_diseases - Diseases.py
2.	https://findmydoctor.mass.gov/- - DbConnection.py
3.	https://book.zocdoc.com/get-started?utm_source=google&utm_medium=cpc_brand&utm_campaign=12793676051&utm_term=zocdoc&utm_content=122847269722&gclid=Cj0KCQiAyracBhDoARIsACGFcS4A6qzB0YXJxWA38QHgLCAzyguZ21J5V2UENmSYWg7mZ8exMcZavekaAoCcEALw_wcB - main.py
4.	https://www.bostonmagazine.com/find-a-doctor/?s=&location=Massachusetts&cat=540 -main.py

Python Scripts:

1.	Using beautiful Soup in python we scrape the necessary data required from the sources stated above and store them in CSV File.
2.	Later this CSV file is cleaned  to exclude duplicate, null values and special characters using cleaning scripts
3.	The cleaned data is inserted into SQL tables which will populate the following tables
  -  Diseases
  -  Doctors
  -  Hospitals
  -  Disease Categories
4.	Please refer to the SQL Scripts folder for the physical model
5.	As part of data Auditing data collected is Visualized using seabron library showing statics of data collected -Visualization Jupyter Source File




# CONTRIBUTORS

1. Rohit Panicker | NUID: 002791446
2. Rohit Paul | NUID: 002908933 
3. Akshatha Patil | NUID: 002657158
