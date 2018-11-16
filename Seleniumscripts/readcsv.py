import csv
import pymysql

conn = pymysql.connect(host='localhost' ,port=3306 , user='root', password='sahana', db='artheeDB')

with open('Pythontestfile2.csv') as csvfile:
    reader=csv.DictReader(csvfile,delimiter=',')
    mycursor = conn.cursor()
    for row in reader:
       sql = "INSERT INTO regtable(Regid,regdate,starttime,endtime,subj,remarks) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (row['Regid'], row['regdate'], row['starttime'], row['endtime'], row['subj'], row['remarks'])
       print(sql)
       mycursor.execute(sql)
       conn.commit()

    conn.close()





