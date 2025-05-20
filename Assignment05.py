
# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   Alex Ngugi, 05/19/2025, Created Script
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
FILE_NAME = "Enrollments.json"
MENU = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

# Define the Data Variables
student_first_name = ''
student_last_name = ''
course_name = ''
student_data = {}
students = []
file = None
menu_choice = ''

# Load data from file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError:
    print("File not found. Starting with an empty list.")
    students = []
except Exception as e:
    print("There was an unexpected error reading the file.")
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
finally:
    if file and not file.closed:
        file.close()

# Main loop
while True:
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("First name must only contain letters.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("Last name must only contain letters.")

            course_name = input("Enter the course name: ")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print(f"You have registered {student_first_name} "
                  f"{student_last_name} for {course_name}.")

        except ValueError as e:
            print(e)
            print("-- Technical Error Message --")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    elif menu_choice == "2":
        print("-" * 50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} "
                  f"is enrolled in {student['CourseName']}")
        print("-" * 50)
        continue

    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print(f"Student {student['FirstName']} {student['LastName']} "
                      f"is enrolled in {student['CourseName']}")
        except TypeError as e:
            print("Please check that the data is a valid JSON format.")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e:
            print("There was a non-specific error!")
            print("-- Technical Error Message --")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file and not file.closed:
                file.close()
        continue

    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4.")

print("Program Ended.")
