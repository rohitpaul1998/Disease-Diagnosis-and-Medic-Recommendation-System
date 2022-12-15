import csv

import openpyxl as openpyxl
import pandas as pd
import xlsxwriter
import MySQLdb
import random

#1.Reading df7 excel - contains hospitals dataset

df7 = pd.read_excel(r"C:\Users\Dell\Documents\Hospitals.xlsx")
#print(df7)

#2. cleaning data in hospital affliations column of the above excel
    #2a. creating a new dataframe dfx
dfx = pd.DataFrame(columns=['Doctor_Id', 'Hospital_Affiliations'])

for index, row in df7.iterrows():
    #print(row['Doctor_Id'], row['Hospital_Affiliations'])
    ID = row['Doctor_Id']
    #print(type(row['Hospital_Affiliations']))
    X = row['Hospital_Affiliations'].split(",")
    for i in X:
        dfx.loc[len(dfx)] = [ID,i]

#3. Removing Duplictes in dataframe
dffinal=dfx.drop_duplicates()

#4. Removing White Spaces in data
def whitespace_remover(dffinal):
    # iterating over the columns
    for i in dffinal.columns:

        # checking datatype of each columns
        if dffinal[i].dtype == 'object':

            # applying strip function on column
            dffinal[i] = dffinal[i].map(str.strip)
        else:

            # if condn. is False then it will do nothing.
            pass
# applying whitespace_remover function on dataframe
whitespace_remover(dffinal)


#5.Creating new column  Id in Hospital_Affiliations dataframe(dffinaldoctors)
dffinal.insert(0, 'Id', range(1, 1 + len(dffinal)))
print(dffinal)

#3. saving the updated dataframe to a csv file
dffinal.to_csv('Hospital_Affiliations_UPDATED_14thDec.csv', index=False)


#5. USING BELOW CODE TO CONNECT TO MYSQL DB !!!!!

db = MySQLdb.connect("localhost","root","Suma$","DDMRS")
cursor = db.cursor()

csv_data = csv.reader(open('Hospital_Affiliations_UPDATED_14thDec.csv'))
header = next(csv_data)

print("Importing file...")

for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO Hospital_Affiliations(Id,Doctor_Id, Hospital_Affliations) VALUES(%s,%s, %s)", row)

db.commit()
cursor.close()
print("Done..")
