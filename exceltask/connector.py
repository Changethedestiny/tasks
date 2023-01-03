import pandas as pd
import mysql.connector as sql
db=sql.connect(host="localhost",user="root",database='excel',password="nagendra@123")

mycursor=db.cursor()
mycursor.execute("select*from excelthree where username='Dulce'")
myresult=mycursor.fetchall()
for column in myresult:
    print(column)


# # we need to strore data into csv
# dic={'user_name':column}
# df=db.DataFrame(dic)
# df_csv=df.to_csv('excelemp.xlsx')