import csv

import openpyxl as openpyxl
import pandas as pd
import xlsxwriter
import MySQLdb
import random


#1.Reading df6 excel - contains hospitals dataset

df6 = pd.read_excel(r"C:\Users\Dell\Documents\Hospitals.xlsx")
#print(df6)


#2.Cleaning ZipCode column to remove unwanted values
df6['Zip_Code'] = df6['Zip_Code'].astype(str).str[:4]

df6['Hospital_Id'] = range(1, 1+len(df6))
print(df6)

#3. Now saving the now cleaned dataframe to a new dataframe
df6pt2 = df6[['City','State','Zip_Code','Hospital_Id']]
# print(df6pt2)

#4. Saving the df6pt2 to a new excel file:
df6pt2.to_csv('PINCODES_STATE_CITY_UPDATED_10thDec.csv', index=False)


#5.USING BELOW CODE TO CONNECT TO MYSQL DB !!!!!

db = MySQLdb.connect("localhost","root","Suma$","DDMRS")
cursor = db.cursor()

csv_data = csv.reader(open('PINCODES_STATE_CITY_UPDATED_10thDec.csv'))
header = next(csv_data)

#print(header)

print("Importing file...")

for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO PINCODES_STATE_CITY(City, State, Zip_Code,Hospital_Id) VALUES(%s, %s, %s,%s)", row)

db.commit()
cursor.close()
print("Done..")
