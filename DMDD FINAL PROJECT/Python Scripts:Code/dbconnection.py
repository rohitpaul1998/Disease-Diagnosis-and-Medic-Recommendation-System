import csv
import pandas as pd
import MySQLdb
import random

#Reading excelfiles to create dataframe1
df1 = pd.read_excel(r"C:\Users\Dell\Documents\Massdoc.xlsx")

#Reading excelfiles to create dataframe2
df2=pd.read_excel(r"C:\Users\Dell\Downloads\zocdoc.xlsx")

#Cleaing the data

#1.Cleaning the doctor name column by spliting it into Doctor_Nmae and Degree
df2['Doctor_Name'].str.split(',',n=1)
df2[['Doctor_Name','Degree']] = df2['Doctor_Name'].str.split(',', n=1, expand=True)

#2.Concating two data frames for doctors since data is collected from two different sources
df3=pd.concat([df1,df2])

#3.Filling Nan with Unknown for those doctors who dont have License Number
df4=df3.fillna({'License_Number':'Unknown'})

#4. Populating Gender column where gender is Nan
df4['Gender'] = pd.Series(
    random.choices(['Male', 'Female','Transgender'], weights=[1, 1,1], k=len(df4)),
    index=df4.index
)
dffinaldoctors=df4.drop(['Practice_Specialities', 'Degree'], axis=1)



#6.Generating new dataframe for Disease Category dataframe from Doctors dataframe(df4)
df6=df4['Practice_Specialities'].str.split(',',expand=True)

#7.Removing duplicates
df6=df6.unstack().drop_duplicates()
df6.to_csv('Disease_Categories.csv')
df7 = pd.read_csv ('Disease_Categories.csv')

#8.Reformatting data to fit in disease_category table
df7.drop(df7.filter(regex="Unname"),axis=1, inplace=True)
df8=df7.rename(columns={"0": "Disease_Category_Name"})
df8['Disease_Category_Id'] = range(1, 1+len(df7))
df9 = df8.reindex(columns=list(df8.columns)[::-1])
df9["Disease_Category_Name"].fillna(" Hepatology", inplace = True)
#print(df9)


#9.Reading excelfiles to create dataframe5
df5 = pd.read_excel(r"C:\Users\Dell\Documents\Hospitals.xlsx")

#10.Cleaning ZipCode column to remove unwanted values
df5['Zip_Code'] = df5['Zip_Code'].astype(str).str[:4]


dffinalhospital = df5[['Hospital_Id','Zip_Code']]

print(dffinalhospital)

dffinalhospital.to_csv('Hospitals_UPDATED_10thDec.csv', index=False)
dffinaldoctors.to_csv('Doctors_UPDATED_14thDec.csv', index=False)

db = MySQLdb.connect("localhost","root","Suma$","DDMRS")
cursor = db.cursor()

csv_data = csv.reader(open('Hospitals_UPDATED_10thDec.csv'))
header = next(csv_data)

#print(header)

print("Importing file...")

for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO Hospitals(Hospital_Id, Zip_Code) VALUES(%s, %s)", row)

db.commit()
cursor.close()
print("Done..")

db = MySQLdb.connect("localhost","root","Suma$","DDMRS")
cursor = db.cursor()

csv_data = csv.reader(open('Doctors_UPDATED_14thDec.csv'))
header = next(csv_data)



print("Importing file...")

for row in csv_data:
    print(row)
    cursor.execute("INSERT INTO Doctors(Doctor_Id, License_Number,Doctor_Name,Gender) VALUES(%s, %s, %s, %s)", row)

db.commit()
cursor.close()
print("Done..")

#Pushing dataframe directly to diseasecategory table
#Create connection to Mysql using creating engine and populating data into respective tables
from sqlalchemy import create_engine

# format: mysql://user:pass@host/db

engine = create_engine("mysql+pymysql://root:Suma$@localhost/DDMRS_BACKUP", pool_pre_ping=True)
df9.to_sql('diseasecategory',con=engine,if_exists='replace',index=False)
