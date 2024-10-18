students={}
while True:
        print("1.Add or Update student info\n2.Display student information\n3.exit")
        choice = int(input("Enter your choice: "))
        if choice==1:
                name=input("Enter student name: ")
                age =int(input("Enter student age: "))
                marks =int(input("Enter marks out of 100: "))
                grade=chr
                if name in students:
                        print("\nUpdating data for",name,"\n")
                else:
                       
                        print("\nAdding new student ",name,"\n")
                        students[name]={"age":age,"Marks":marks,"Grade":grade}
        elif choice==2:
                if not students:
                        print("\nStudent data not found:\n")
                for name,details in students.items():
                        if marks>=100 and marks<80:
                            grade='A'
                        elif marks>=80 and marks<60:
                            grade='B'
                        elif marks>=60 and marks<40:
                            grade='C'
                        else:
                            grade='F'
                        
                        print("name:",name,"Age:",details['age'],"Marks:",details['Marks'],"Grade:",grade)
        elif choice==3:
                break
        else:
                print("Invalid option")