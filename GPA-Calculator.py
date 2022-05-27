terms_number = int(input("Enter number of terms: "))

counter = 1
total_GPA = 0
while counter <= terms_number:                               #term loop
    print("Term ", counter ," :")
    courses = int(input("Enter number of courses: "))

    course_counter = 1
    grade_number = 1
    total_points_value = 0
    credit_hours = int(courses) * 3 
    while course_counter <= courses:                        #courses loop
        grade = input("Enter grade " + str(grade_number) + ": ")

        if (grade == "A+"):
            points_value = 12
        elif (grade == "A"):
            points_value = 11.5
        elif (grade == "A-"):
             points_value = 11
        elif (grade == "B+"):
            points_value = 10
        elif (grade == "B"):
             points_value = 9
        elif (grade == "B-"):
            points_value = 8
        elif (grade == "C+"):
             points_value = 7 
        elif (grade == "C"):
            points_value = 6
        elif (grade == "C-"):
             points_value = 5 
        elif (grade == "D+"):
             points_value = 4 
        elif (grade == "D"):
            points_value = 3
        elif (grade == "F"):
             points_value = 0 

        total_points_value = total_points_value + points_value
        grade_number = grade_number +1
        course_counter = course_counter + 1

    GPA = total_points_value / credit_hours
    print("Term ", counter, " GPA is: ", GPA ,"\n")
    counter = counter + 1
    total_GPA = total_GPA + GPA

# overall GPA
overall_GPA = total_GPA / terms_number
print("Your overall GPA is: ", overall_GPA )

# descriptive_grade
if ( 3.6 < overall_GPA < 4):
    descriptive_grade = "Excellent"
elif ( 3 < overall_GPA < 3.6):
    descriptive_grade = "Very Good"
elif ( 2.6 < overall_GPA < 3):
    descriptive_grade = "Good"
elif ( 2 < overall_GPA < 2.6):
    descriptive_grade = "Pass"
print("Your grade is: ",  descriptive_grade)