from tkinter import *
import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    port='3306',
    database='form'
)
mycursor =mydb.cursor()
mycursor.execute('select * from register_table')
register_table =mycursor.fetchall()
for register_table in register_table:
    print(register_table)
    print('firstname'+ register_table[1])
    print('lastname'+ register_table[2])
    print('mailid' + register_table[3])
    print('phone' + register_table[4])
    print('gender' + register_table[5])

root = Tk()
root.geometry("500x300")
root.configure(bg='#003e53')

def getvals():
    print("Accepted")

Label(root, text="PYTHON REGISTRATION  FORM", font= "arial 15 bold",bg='#003e53',fg="white").grid(row=0,column=1)
firstname = Label(root, text="First name")
lastname = Label(root, text="Last name")
mailid = Label(root, text="Mailid")
password=Label(root,text="Password")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")

Label(text="first name").grid(row=1, column=1, padx=90)
Label(text="lastname").grid(row=2, column=1,padx=90)
Label(text="mailid").grid(row=3, column=1,padx=90)
Label(text="password").grid(row=4,column=1,padx=90)
Label(text="phone").grid(row=5, column=1,padx=90)
Label(text="gender").grid(row=6, column=1,padx=90)

firstnamevalue = StringVar()
lastnamevalue = StringVar()
mailidvalue =  StringVar()
passwordvalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
checkvalue = StringVar()


firstnameentry= Entry(root, textvariable =firstnamevalue)
lastnameentry= Entry(root, textvariable =lastnamevalue)
mailidentry= Entry(root, textvariable =mailidvalue)
passwordentry=Entry(root,textvariable =passwordvalue)
phoneentry= Entry(root, textvariable =phonevalue)
genderentry= Entry(root, textvariable =gendervalue)

firstnameentry.grid(row=1, column=2, pady=10)
lastnameentry.grid(row=2, column=2, pady=10)
mailidentry.grid(row=3, column=2, pady=10)
passwordentry.grid(row=4,column=2, pady=10)
phoneentry.grid(row=5, column=2, pady=10)
genderentry.grid(row=6, column=2, pady=10)

checkbtn= Checkbutton(text="remember me?", variable=checkvalue)
checkbtn.grid(row=7, column=2)
Button(text="submit", command=getvals).grid(row=11 , column=2)
Button(text="Return", command=getvals).grid(row=11,column=3)

root.mainloop()