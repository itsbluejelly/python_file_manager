# IMPORTING REQUIRED FILES
from classes import Student as StudentClassFile
from classes import FileHandler as FileHandlerClassFile

# GETTING REQUIRED CLASSES
Student = StudentClassFile.Student
FileHandler = FileHandlerClassFile.FileHandler

# A FUNCTION TO ADD A STUDENT TO THE DATABASE
def add_student():
    # GETTING STUDENT DETAILS WHICH ARE ADMISSION NUMBER, NAME, AGE AND NUMBER OF UNITS TAKEN
    student_admission_number = 0
    student_name = ""
    student_age = 0
    student_total_units = 0

        # STUDENT ADMISSION NUMBER
    while True:
        try:
            student_admission_number = int(input("\t1. What is the admission number of the student: "))

            if not student_admission_number:
                raise ValueError
        except ValueError:
            print("\n\t\tThe student admission number must be an integer with a value\n")
        else:
            break

        # STUDENT NAME
    while True:
        try:
            student_name = input("\t2. What is the name of the student: ").strip().title()

            if(student_name == ""):
                raise ValueError
        except ValueError:
            print("\n\t\tThe student name must have a value\n")
        else:
            break
        
        # STUDENT AGE
    while True:
        try:
            student_age = int(input(f"\t3. What is {student_name}'s age: "))

            if(student_age < 18):
                raise ValueError
        except ValueError:
            print("\n\t\tThe student age must be an integer greater than or equal to 18\n")
        else:
            break
        
        # STUDENT TOTAL UNITS
    while True:
        try:
            student_total_units = int(input(f"\t4. How many units are {student_name} taking: "))

            if(student_total_units <= 0):
                raise ValueError
        except ValueError:
            print("\n\t\tThe student must take a unit in the school, and the value must be an integer\n")
        else:
            break

    # IF THE STUDENT AGE, NAME AND TOTAL UNITS ARE FINE, CREATE A STUDENT
    student = Student(student_admission_number, student_name, student_age, student_total_units)

    # POPULATE THE STUDENT INSTANCE WITH RECORDED UNITS
    print("\nPlease fill in the values accordingly: ")
    student.populate_recorded_units()

    # GET THE TOTAL AND AVERAGE MARK FROM THE RECORDED UNITS
    print("\nCalculating total and average marks...")
    student.calculate_total_mark()
    student.calculate_average_mark()

    # GET THE AVERAGE GRADE FROM AVERAGE MARK
    print("\nCalculating average grade...")
    student.calculate_average_grade()
        
    # RECORD THE STUDENT DATA AND DISPLAY IT AFTER CREATION
    FileHandler.add_student_data("student_data.csv", student)
    FileHandler.add_student_units("student_units.csv", student)
    student.get_student_data()

# A FUNCTION TO READ DATA FROM THE DATABASE
def get_student():
    # GETTING CHOICE ON HOW TO READ THE DATA
    while True:
        try:
            choice_of_reading = input("\nHow would you like to read the data\n\t1. [A] to read a single student via admission number\n\t2. [R] to read a random student\n\t3. [E] to read every student: ").strip().title()
        
            if((choice_of_reading != "A") and (choice_of_reading != "Admission") and (choice_of_reading != "R") and (choice_of_reading != "Random") and (choice_of_reading != "E") and (choice_of_reading != "Every")):
                raise ValueError
        except ValueError:
            print("\n\t\tInvalid choice, try again\n")
        else:
            break

    # MAKING RIGHT DECISION BASED ON SAID CHOICE
    if((choice_of_reading == "A") or (choice_of_reading == "Admission")):
        # GET THE STUDENT ADMISSION NUMBER
        student_admission_number = 0

            # ADMISSION NUMBER
        while True:
            try:
                student_admission_number = int(input("\nWhat is the admission number of the student: "))

                if not student_admission_number:
                    raise ValueError
            except ValueError:
                print("\n\tThe student admission number must be an integer with a value\n")
            else:
                break

        # GETTING THE STUDENT DATA
        print(f"\nFetching a student's data with admission number {student_admission_number}...")
        FileHandler.get_admitted_student_data("student_data.csv", student_admission_number)
        FileHandler.get_admitted_student_units("student_units.csv", student_admission_number)
    elif((choice_of_reading == "R") or (choice_of_reading == "Random")):
        # GETTING A RANDOM STUDENT
        print("\nFetching a random student's data...")
        FileHandler.get_random_student_data("student_data.csv", "student_units.csv")
    else:
        ...

# A FUNCTION TO UPDATE A STUDENT WITHIN THE DATABASE

# A FUNCTION TO DELETE A STUDENT FROM THE DATABASE

# MAIN FUNCTION
def main():
    print("This is a program meant to help you organise and enter information about a student\n")

    # CHECKING THE RIGHT COURSE OF ACTION
    while True:
        try:
            choice_of_action = input("What course of action would you like to take?\n\t1. [A] to Add or create a student\n\t2. [R] to Read a certain number of students\n\t3. [U] to Update a certain student's data\n\t4. [D] to Delete a certain student: ").strip().title()

            if((choice_of_action != "A") and (choice_of_action != "Add") and (choice_of_action != "R") and (choice_of_action != "Read") and (choice_of_action != "U") and (choice_of_action != "Update") and (choice_of_action != "D") and (choice_of_action != "Delete")):
                raise ValueError
        except ValueError:
            print("\n\t\tInvalid choice, try again\n")
        else:
            break

    # CARRYING OUT RIGHT ACTION BASED ON THE CHOICE GIVEN
    if((choice_of_action == "A") or (choice_of_action == "Add")):
        print("\nCurrently adding a new student...")
        add_student()
    elif((choice_of_action == "R") or (choice_of_action == "Read")):
        print("\nCurrently fetching a recorded student...")
        get_student()
    else:
        print("In Development")
    
# CHECK IF FILE HAS MAIN FUNCTION AND RUN IT
if __name__ == "__main__":
    main()

    # VALIDATING RERUN OPTION
    while True:
        try:
            rerun_program = input("Would you like to rerun this program?\n\t1. [Y] for Yes\n\t2. [N] for No: ").strip().title()

            if((rerun_program != "Y") and (rerun_program != "N") and (rerun_program != "Yes") and (rerun_program != "No")):
                raise ValueError
        except ValueError:
            print("\n\t\tInvalid choice, try again\n")
        else:
            if((rerun_program == "N") or (rerun_program == "No")):
                break
            elif((rerun_program == "Y") or (rerun_program == "Yes")):
                main()
            else:
                pass
