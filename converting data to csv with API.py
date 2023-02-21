from flask import Flask
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(host = 'localhost' , database ='postgres' ,
port= '5432', user ='postgres' , password = 'database')

cur = conn.cursor()
@app.route("/convert",methods =['POST','GET'])
def convert():
    try:
        sql = "copy cricbuzz to stdout CSV header;"
        with open("E://player_list.csv", "w") as file:
            cur.copy_expert(sql,file)
            print('Converted to CSV File')
    except  Exception as error:
        print(error)  
    return 'successful conversion'

if (__name__) == '__main__':
    app.run()
conn.commit()
conn.close()