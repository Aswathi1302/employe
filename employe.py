import mysql.connector
mydb = mysql.connector.connect(host='localhost',user='root',password='',database='employes')
mycursor=mydb.cursor()
while True:
    print("select an option from the menu")
    print("1. add employe")
    print("2.view employe")
    print("3.search employe")
    print("4.upadte employe")
    print("5. delete employe")
    print("6.exit")

    choice=int(input("enter your choice:-"))
    if(choice==1):
        print("student enter selected")
        empcode=input("enter a code:")
        empname=input("enter name:-")
        designation=input("enter designation:-")
        salary=input("enter salary:- ")
        compney_name=input("enter compney_name:-")
        mobile=input("enter mobile:-")
        email=input("enter email:-")
        password=input("enter password:- ")
        sql="INSERT INTO `employe`(`empcode`, `empname`, `designation`, `salary`, `compney_name`, `mobile`, `email`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        data=(empcode,empname,designation,salary,compney_name,mobile,email,password)
        mycursor.execute(sql,data)
        mydb.commit()
        print("insert successfully.......")
    elif(choice==2):
        print("view employe")
        sql="SELECT * FROM `employe` "
        mycursor.execute(sql)
        result=mycursor.fetchall()
        for i in result:
            print(i)
    elif(choice==3):
        print("search a student")
    elif(choice==4):
        print("update student")
    elif(choice==5):
        print("delet student")    
    elif(choice==6):
        break                