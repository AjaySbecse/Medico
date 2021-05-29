import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="barathg",
  database="medico"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT a.name , b.patient_mail ,b.status from patient a, consult b where a.mail =  b.patient_mail and b.doctor_id= '101' ")
#mycursor.execute("SELECT * from consult ")
myresult = mycursor.fetchall()

print(myresult)

