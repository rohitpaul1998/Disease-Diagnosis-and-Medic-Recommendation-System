# Import necessary packages
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
#import lxml
import MySQLdb
import csv
import sys

# Site URL
url="https://en.wikipedia.org/wiki/List_of_infectious_diseases"

# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse HTML code for the entire site
soup = BeautifulSoup(html_content, "html.parser")

# On site there is a table with the class "sortable"
# The following line will generate a list of HTML content for each table
dis = soup.find_all("table", attrs={"class": "sortable"})
#print("Number of tables on site: ",len(dis))

# Lets go ahead and scrape first table with HTML code dis[0]
table1 = dis[0]

# the head will form our column names
body = table1.find_all("tr")

# Head values (Column names) are the first items of the body list
head = body[0] # 0th item is the header row

body_rows = body[1:] # All other items becomes the rest of the rows

# Lets now iterate through the head HTML code and make list of clean headings

# Declare empty list to keep Columns names
headings = []

for item in head.find_all("th"): # loop through all th elements
    # convert the th elements to text and strip "\n"
    item = (item.text).rstrip("\n")
    # append the clean column name to headings
    headings.append(item)



all_rows = [] # will be a list for list for all rows

for row_num in range(len(body_rows)): # A row at a time
    row = [] # this will old entries for one row
    for row_item in body_rows[row_num].find_all("td"): #loop through all row entries
        # row_item.text removes the tags from the entries
        # the following regex is to remove \xa0 and \n and comma from row_item.text
        # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
        aa = re.sub("(\xa0)|(\n)|,","",row_item.text)
        #append aa to row - note one row entry is being appended
        row.append(aa)
    # append one row to all_rows
    all_rows.append(row)

# We can now use the data on all_rows and headings to make a table
# all_rows becomes our data and headings the column names
df = pd.DataFrame(data=all_rows,columns=headings)
#shows the first few rows as a preview in the dataframe
#print(df)

#
#
# # Reformat the data to fit the tables of the database schema
# # Modifying any column's character limit in the dataframe
#
# #reformatting 'Infectious agent' column by limitting the character length to 132 characters
df['Infectious agent'] = df['Infectious agent'].str[:132]
#reformatting 'Vaccine(s)' column to take in only 14 character long values
df['Vaccine(s)'] = df['Vaccine(s)'].str[:14]


#
# # Auditing quality of data gathered
# # 1. Audit Validity/ Accuracy
# # 2. Audit Completeness
# # 3. Audit Consistency/Uniformity
#
# #Auditing validity
#
# #To validate the accuracy of our scraped data, below is the URL for our source where the table of infectious diseases is present.
#
# #URL: https://en.wikipedia.org/wiki/List_of_infectious_diseases
#
# #For example, the first record in our dataframe is "Acinetobacter baumannii". When searched in google, we get the below results:
#
# #CDC info: https://www.cdc.gov/hai/organisms/acinetobacter.html
#
# #Virginia.gov info: https://www.vdh.virginia.gov/epidemiology/epidemiology-fact-sheets/acinetobacter-infection/#:~:text=Symptoms%20of%20a%20bloodstream%20infection,and%20pus%20around%20the%20wound
#
#
#
#
# #Auditing Completeness & Auditing Uniformity
#
# #Here, we are cleaning data to include values wherever there is an empty cell or exclude unwanted characters that don't make sense.
#
# #Logic for data cleaning as follows:
#
# #Cleaing all these columns' values to see if data is getting modified/replaced.
# #UPDATE: commenting below logic since, clean was successful.
df['Infectious agent'] = df['Infectious agent'].str.replace('á','a') #yes it works
df['Infectious agent'] = df['Infectious agent'].str.replace(';','') #yes it works
df['Infectious agent'] = df['Infectious agent'].str.replace('Yes','NA') #yes it works
df['Infectious agent'] = df['Infectious agent'].str.replace(r'[41]','') #yes it works
df['Infectious agent'] = df['Infectious agent'].str.replace('usually','') #yes it works
df['Infectious agent'] = df['Infectious agent'].str.replace(r'[','') #yes it works
df['Infectious agent'] = df['Infectious agent'].str.replace(r']','') #yes it works
df['Common name'] = df['Common name'].str.replace(';','') #yes it works
df['Common name'] = df['Common name'].str.replace('–','') #yes it works
df['Common name'] = df['Common name'].str.replace('ä','a') #yes it works
df['Common name'] = df['Common name'].str.replace('’','') #yes it works
df[['Common name','Signs and symptoms','Diagnosis','Treatment','Vaccine(s)']] = df[['Common name','Signs and symptoms','Diagnosis','Treatment','Vaccine(s)']].fillna('NA') #yes it works
df['Signs and symptoms'] = df['Signs and symptoms'].str.replace('–',' to ') #yes it works
df['Signs and symptoms'] = df['Signs and symptoms'].str.replace('ó','o') #yes it works
df['Signs and symptoms'] = df['Signs and symptoms'].str.replace('°',' degrees ') #yes it works

#print(df.head())
#
# #inserting NaN values in the cells wherever empty
import numpy as np
df2 = df.replace(r'^\s*$', np.nan, regex=True)
#print(df2)
#
#
#Now "df2" is my variable that stores updated dataframe having NaN values
#Using df2, I am replacing NaN values with appropriate data under symptoms column

df2[['Signs and symptoms']] = df2[['Signs and symptoms']].fillna('No symptoms found')

#Now "df2" is my variable that stores updated dataframe having NaN values
#Using df2, I am replacing NaN values with appropriate data under diagnosis column

df2[['Diagnosis']] = df2[['Diagnosis']].fillna('No diagnosis found')

#Now "df2" is my variable that stores updated dataframe having NaN values
#Using df2, I am replacing NaN values with appropriate data under treatment column

df2[['Treatment']] = df2[['Treatment']].fillna('No treatment found')

#renaming "Vaccine(s)" column as "Vaccine availability"
df2 = df2.rename(columns={'Vaccine(s)': 'Vaccine_availability'})

#print(df2)
#
# #renaming all columns into different names
df2 = df2.rename(columns={'Infectious agent': 'Disease_agent'})
df2 = df2.rename(columns={'Common name': 'Disease_name'})
df2 = df2.rename(columns={'Signs and symptoms': 'Signs_and_symptoms'})

#print(df2)
#
#creating a new dataframe df3 to only specify some columns in my diseases table
df3 = df2[['Disease_name','Signs_and_symptoms','Diagnosis','Treatment']]
#print(df3) -- diseases dataframe

#adding a new column to diseases table "Disease_Id"
df3.insert(0, 'Disease_Id', range(1, 1 + len(df3)))
#print(df3)



# #Data cleaning is done for Diseases table
# #Now exporting diseases dataframe in CSV
df3.to_csv('List_of_Infectious_Diseases_post_cleaning_24Nov2022_UPDATED.csv', index=False, encoding='utf-8')



# BELOW IS THE CODE FOR INSERTING ABOVE CSV FILES FOR INFECTIOUS DISEASES (df3) AND CATEGORIES (df4) TO MYSQL DB TABLES


db = MySQLdb.connect("localhost","root","Suma$","DDMRS")
cursor = db.cursor()

csv_data = csv.reader(open('List_of_Infectious_Diseases_post_cleaning_24Nov2022_UPDATED.csv'))
header = next(csv_data)

print("Importing the file...")
Disease_name={'Acinetobacter infections':18,'Actinomycosis':18,'Adenovirus infection':19,'African sleeping sickness (African trypanosomiasis)':19,'AIDS (acquired immunodeficiency syndrome)':18,'Amoebiasis':19,'Anaplasmosis':19,'Angiostrongyliasis':18,'Anisakiasis'
:25,'Anthrax':37,'Arcanobacterium haemolyticum infection':37,'Argentine hemorrhagic fever':12,'Ascariasis':14,'Aspergillosis':14,'Astrovirus infection':15,'Babesiosis':66,
'Bacillus cereus infection':66,
'Bacterial meningitis':66,
'Bacterial pneumonia':66,
'Bacterial vaginosis':66,
'Bacteroides infection':38,
'Balantidiasis':38,
'Bartonellosis':38,
'Baylisascaris infection':38,
'BK virus infection':38,
'Black piedra':38,
'Blastocystosis':66,
'Blastomycosis':66,
'Bolivian hemorrhagic fever':66,
'Botulism (and Infant botulism)':38,
'Brazilian hemorrhagic fever':50,
'Brucellosis':50,
'Bubonic plague':28,
'Burkholderia infection':28,
'Buruli ulcer':28,
'Calicivirus infection (Norovirus and Sapovirus)':28,
'Campylobacteriosis':28,
'Candidiasis (Moniliasis Thrush)':28,
'Capillariasis':18,
'Dental caries':18,
"Carrion's disease":3,
'Cat-scratch disease':3,
'Cellulitis':3,
'Chagas disease (American trypanosomiasis)':18,
'Chancroid':18,
'Chickenpox':17,
'Chikungunya':17,
'Chlamydia':29,
'Chlamydophila pneumoniae infection (Taiwan acute respiratory agent or TWAR)':66,
'Cholera':66,
'Chromoblastomycosis':136

}

for row in csv_data:

    try:
      row.append(Disease_name[row[1]])
      print(row)
    except Exception as e:
        print(row)

    cursor.execute("INSERT INTO Diseases(Disease_Id, Disease_name, Signs_and_symptoms, Diagnosis, Treatment,Disease_Category_Id) VALUES(%s, %s, %s, %s,%s,%s)",row)
    db.commit()

    print("Done..")
cursor.close()







