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
        print("search a employe")
        empcode=input("enter a code:-")
        sql="SELECT * FROM `employe` WHERE `empcode`="+empcode
        mycursor.execute(sql)
        result=mycursor.fetchall()
        print(result)

    elif(choice==4):
        print("update employe")
        empcode=input("enter the employe code:")
        empname=input("enter name to be upadted:-")
        designation=input("enter designation to be upadted:-")
        salary=input("enter salary to be upadted:- ")
        compney_name=input("enter compney_name to be upadted:-")
        mobile=input("enter mobile to be upadted:-")
        email=input("enter email to be upadted:-")
        password=input("enter password to be upadted:- ")
        sql="UPDATE `employe` SET `empname`='"+empname+"',`designation`='"+designation+"',`salary`='"+salary+"',`compney_name`='"+compney_name+"',`mobile`='"+mobile+"',`email`='"+email+"',`password`='"+password+"' WHERE `empcode`=" +empcode
        mycursor.execute(sql)
        mydb.commit()
        print("Data updated successfully....")

    elif(choice==5):
        print("delet employe")    
    elif(choice==6):
        break                