import pandas as pd
import psycopg2

conn = psycopg2.connect(host = 'localhost' , database ='postgres' ,
port= '5432', user ='postgres' , password = 'database')

cur = conn.cursor()

# sql = "copy player to stdout CSV header;"
# with open("E://cricbuzz.csv", "w") as file:
#     cur.copy_expert(sql,file)
       
df = pd.read_sql_query('select * from "cricbuzz"',conn)
# query = "COPY students TO '/tmp/student1.csv' CSV HEADER;"
print(df)

conn.commit()
conn.close()