import pandas as pd
import mysql.connector as sql
db=sql.connect(host="localhost",user="root",database='excel',password="nagendra@123")
cursor=db.cursor()

query="select place from excelthree"
cursor.execute(query)

myallData=cursor.fetchall()

all_place=[]
for place in myallData:
    all_place.append(place)

#we need to strore data into csv
dic={'user_name':all_place}
df=db.DataFrame(dic)
df_csv=df.to_csv('excelemp.xlsx')