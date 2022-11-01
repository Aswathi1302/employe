while True:
    print("select an option from the menu")
    print("1. add employe")
    print("2.view employe")
    print("3.search employe")
    print("4.upadte employe")
    print("5. delete employe")
    print("6.exit")

    choice=int(input("enter your choice"))
    if(choice==1):
        print("student enter selected")
        empcode=input("enter a code")
        empname=input("enter name")
        designation=input("enter designation")
        salary=input("enter salary ")
        compney_name=input("enter compney_name")
        mobile=input("enter mobile")
        email=input("enter email")
        password=input("enter password ")
        sql="INSERT INTO `students`(`name`, `rollno`, `admNo`, `college`) VALUES (%s,%s,%s,%s)"
    elif(choice==2):
        print("view student")
    elif(choice==3):
        print("search a student")
    elif(choice==4):
        print("update student")
    elif(choice==5):
        print("delet student")    
    elif(choice==6):
        break                