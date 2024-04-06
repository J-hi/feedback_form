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
contact=input("contact number:")
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
