print("---------------Feedback Form------------------")
#
first_name=input("first name: ")
if(first_name.isdigit()):
    print("invalid input")
    first_name=input("first name: ")
#
last_name=input("last name: ")
if(last_name.isdigit()):
    print("invalid input")
    last_name=input("last name: ")
#
email=input("email:")
#
contact=int(input("contact number:"))
if(len(str(contact))!=10):
    print("please enter a valid contact numbeer.")
    contact=int(input("contact number:"))
#
enroll_id=input("enrollment no:")
#
print("select school : ")
print("1.SOE\n2.SOM\n3.SOD\n4.SOL")
school = int(input("-: "))
if school ==1:
    print("SOE")
if school ==2:
    print("SOM")
if school ==3:
    print("SOD")
if school ==4:
    print("SOL")

#
programme=input("programme:")
if(programme.isdigit()):
    print("invalid input")
    programme=input("programme:")
#
discipline=input("discipline:")
if(discipline.isdigit()):
    print("invalid input")
    discipline=input("discipline:")
#
course=input("course:")
if(course.isdigit()):
    print("invalid input")
    course=input("course:")
#
course_code=input("course code")

#
faculty=input("faculty name:")
if(faculty.isdigit()):
    print("invalid input")
    faculty=input("faculty name:")
#
sem=input("semester:")

print("______________________________Feedback Please____________________________________________")


#add feedback questions with input statement

Question_1=input("1. Are you satisfied with the overall teaching of the Course:")
Question_2=input("2. Subject knowledge of the Cource Lead:")
Question_3=input("3. Communication skils of the Course Lead:")
Question_4=input("4. Lectures were delivered at a pace that is:")
Question_5=input("5. Would you like to have another Course:")
Question_6=input("6. The Course was organised in a way that helped me to learn:")
Question_7=input("7. Overall rating for the Course:")
Question_8=input("8. Overall rating for the Course Lead:")

print("_______________THANK YOU_________________ ")
print("___________________________________________________________________________________")

