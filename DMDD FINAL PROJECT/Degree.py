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
#Cleaning data to Populate Degree Table
print(df4)
df6=df4['Degree'].str.split('. or',expand=True)
df6.to_csv('Degree.csv')
df7 = pd.read_csv ('Degree.csv')

df7.drop(df7.filter(regex="Unname"),axis=1, inplace=True)
df8=df7.rename(columns={"0": "Doctor_Degree"})
df8['Doctor_Id'] = range(1, 1+len(df7))
df10=df8.drop(["1"],axis=1)
print(df10)

#Cleaning data to populate Practice_Specialities table
df11=df4[['Practice_Specialities','Doctor_Id']]
print(df11.values.tolist())
df11.explode(['Practice_Specialities', 'Doctor_Id'])
df13=df11.assign(Practice_Specialities=df11['Practice_Specialities'].str.split(',')).explode('Practice_Specialities')
df14=df13.drop_duplicates()



def whitespace_remover(df14):
    # iterating over the columns
    for i in df14.columns:

        # checking datatype of each columns
        if df14[i].dtype == 'object':

            # applying strip function on column
            df14[i] = df14[i].map(str.strip)
        else:

            # if condn. is False then it will do nothing.
            pass


# applying whitespace_remover function on dataframe
whitespace_remover(df14)

# printing dataframe
print(df14)
from sqlalchemy import create_engine

# format: mysql://user:pass@host/db

engine = create_engine("mysql+pymysql://root:Suma$@localhost/DDMRS_BACKUP", pool_pre_ping=True)

df10.to_sql('degree',con=engine,if_exists='replace',index=False)
df14.to_sql('practice_specialities',con=engine,if_exists='replace',index=False)