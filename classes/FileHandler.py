# IMPORTING REQUIRED MODULES AND FILES
import csv
import os
import random

# A CLASS FOR ALL FILE FUNCTIONS
class FileHandler:
    # A FUNCTION TO ADD STUDENT DATA TO A FILE
    @classmethod
    def add_student_data(cls, fileName, student):
        # CHECKING IF PARAMETER VALUES ARE OK
        if(type(fileName) != type("fileName")):
            raise TypeError(f"The file name, {fileName}, must be a string")
        elif(fileName == ""):
            raise ValueError("The file name, 1st parameter, must have a value")
        
        # CHECK IF FOLDER TO FILE EXISTS, IF SO, CHECK IF STUDENT EXISTS IN DATABASE, IF NOT, CREATE THE FILE
        print("\nChecking if the folder to student file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        filePath = os.path.join(folderPath, fileName)

        if(os.path.exists(filePath)):
            print(f"Folder and file exists, checking if {student._name}'s data is already in database...")
            
            # CHECK IF STUDENT IS ALREADY IN DATABASE, IF SO, RAISE AN ERROR
            with open(filePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # IF 1ST ROW OR AN EMPTY LINE, SKIP
                    if((len(row) == 0) or (row[0] == "Admission number")):
                        continue
                
                    student_admission_number = int(row[0])    
                    
                    # IF ADMISSION NUMBERS ARE SIMILAR, RAISE ERROR, IF NOT SHOW SUCCESS MESSAGE
                    if(student._admission_number == student_admission_number):
                        print(f"\n\t{student._name}'s data already recorded\n")
                        return
                    else:
                        print(f"Data doesn't exist in database, attempting to add {student._name}'s data...")
        else:
            print("Folder not found, creating new folder...")
            os.mkdir(folderPath)
            print("Folder to student file created successfully, creating new file...")

            with open(filePath, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Admission number", "Name", "Age", "Total units", "Total mark", "Average mark", "Average grade"])

                print(f"File created successfully, attempting to add {student._name}'s data...")
        
        # IF EVERYTHING IS OKAY, ADD THE ROW OF DATA
        with open(filePath, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([student._admission_number, student._name, student._age, student._total_units, student.total_mark, student.average_mark, student.average_grade])
            
            print(f"\n{student._name}'s data added to database successfully...\n")

    # A FUNCTION TO ADD STUDENT UNITS TO A FILE
    @classmethod
    def add_student_units(cls, fileName, student):
        # CHECKING IF PARAMETER VALUES ARE OK
        if(type(fileName) != type("fileName")):
            raise TypeError(f"The file name, {fileName}, must be a string")
        elif(fileName == ""):
            raise ValueError("The file name, 1st parameter, must have a value")
        
        # CHECK IF FILE IN SUBSEQUENT EXISTS, IF SO, CHECK IF STUDENT EXISTS IN DATABASE, IF NOT, CREATE THE FILE
        print("\nChecking if the student units file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        filePath = os.path.join(folderPath, fileName)

        if(os.path.exists(filePath)):
            print(f"File exists, checking if {student._name}'s units are already in database...")
            
            # CHECK IF STUDENT IS ALREADY IN DATABASE, IF SO, RAISE AN ERROR
            with open(filePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # IF 1ST ROW OR AN EMPTY LINE, SKIP
                    if((len(row) == 0) or (row[0] == "Admission number")):
                        continue
                
                    student_admission_number = int(row[0])    
                    
                    # IF ADMISSION NUMBERS ARE SIMILAR, RAISE ERROR, IF NOT SHOW SUCCESS MESSAGE
                    if(student._admission_number == student_admission_number):
                        print(f"\n\t{student._name}'s units already recorded\n")
                        return
                    else:
                        print(f"Data doesn't exist in database, attempting to add {student._name}'s units data...")
        else:
            print("File not found, creating new file...")
            
            with open(filePath, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Admission number", "\t", "Recorded units"])

                print(f"File created successfully, attempting to add {student._name}'s units data...")
        
        # IF EVERYTHING IS OKAY, ADD THE ROW OF DATA
        with open(filePath, "a", newline="") as file:
            writer = csv.writer(file)
            
            writer.writerow([
                student._admission_number, 
                "\t", 
                "; ".join([str(unit) for unit in student.recorded_units])
            ])
            
            print(f"\n{student._name}'s units added to database successfully...\n")
    
    # A FUNCTION TO READ ADMITTED STUDENT DATA FROM A FILE AND RETURN DATA
    @classmethod
    def get_admitted_student_data(cls, fileName, admission_number):
        # CHECK IF THE PARAMETERS ARE OKAY
            # FILENAME
        if(type(fileName) != type("fileName")):
            raise TypeError(f"The file name, {fileName}, must be a string")
        elif(fileName == ""):
            raise ValueError("The file name, 1st parameter, must have a value")
        
            # ADMISSION NUMBER
        if(type(admission_number) != type(123)):
            raise TypeError(f"The admission number, {admission_number}, must be an integer")
        elif not admission_number:
            raise ValueError("The admission number, 2nd parameter, must have a value")
        
        # CHECK IF PATH TO FILE TO READ FROM EXISTS, IF SO, CHECK IF STUDENT EXISTS, IF NOT, RAISE ERROR
        print("\nChecking if the student file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        filePath = os.path.join(folderPath, fileName)

        if(os.path.exists(filePath)):
            print(f"File exists, checking if {admission_number}'s data is already in database...")
            
            # CHECK IF STUDENT IS ALREADY IN DATABASE, IF SO, READ THE DATA
            with open(filePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # IF 1ST ROW OR AN EMPTY LINE, SKIP
                    if((len(row) == 0) or (row[0] == "Admission number")):
                        continue
                
                    student_admission_number = int(row[0])    
                    
                    # IF ADMISSION NUMBERS ARE SIMILAR, READ THE DATA
                    if(student_admission_number == admission_number):
                        print(f"Data exists in database, attempting to read {admission_number}'s data...")

                        # GET THE STUDENT DATA FROM THE ROW
                        [student_name, student_age, student_total_units, student_total_mark, student_average_mark, student_average_grade] = row[1::]
                        
                        # PRINT GENERAL DATA
                        print(f"\nStudent details: \n\t[\n\t\tStudent name: {student_name},\n\t\tStudent Age: {student_age},\n\t\tStudent Total Units: {student_total_units},\n\t]\n")

                        # SHOW TOTAL AND AVERAGE MARK
                        print(f"\t-> {student_name}'s total mark obtained from the {student_total_units} units is: {float(student_total_mark):,.2f}")
                        print(f"\t-> {student_name}'s average mark obtained from the {float(student_total_mark):,.2f} total mark is: {float(student_average_mark):,.2f}\n")

                        # SHOW AVERAGE GRADE
                        print(f"\t-> {student_name}'s average grade from an average mark of {float(student_average_mark):,.2f} is: {student_average_grade}\n")
                        
                        # RETURN DATA, WHICH IS THE ADMISSION NUMBER, NAME, AGE AND TOTAL UNITS
                        return {
                            "admission_number": student_admission_number,
                            "name": student_name,
                            "age": int(student_age),
                            "total_units": int(student_total_units),
                            "total_mark": float(student_total_mark),
                            "average_mark": float(student_average_mark),
                            "average_grade": student_average_grade,
                        }
                        
        else:
            print(f"\n\tError: {fileName} not found 😞\n")
            return
            
    # A FUNCTION TO READ ADMITTED STUDENT UNITS FROM A FILE AND RETURN RECORDED UNITS
    @classmethod
    def get_admitted_student_units(cls, fileName, admission_number):
        # CHECK IF THE PARAMETERS ARE OKAY
            # FILENAME
        if(type(fileName) != type("fileName")):
            raise TypeError(f"The file name, {fileName}, must be a string")
        elif(fileName == ""):
            raise ValueError("The file name, 1st parameter, must have a value")
        
            # ADMISSION NUMBER
        if(type(admission_number) != type(123)):
            raise TypeError(f"The admission number, {admission_number}, must be an integer")
        elif not admission_number:
            raise ValueError("The admission number, 2nd parameter, must have a value")
        
        # CHECK IF PATH TO SUBSEQUENT FILE TO READ FROM EXISTS, IF SO, CHECK IF STUDENT EXISTS, IF NOT, RAISE ERROR
        print("\nChecking if the student units file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        filePath = os.path.join(folderPath, fileName)

        if(os.path.exists(filePath)):
            print(f"File exists, checking if {admission_number}'s units are already in database...")
            # A LIST CONTAINING THE RECORDED UNITS
            recorded_units = []
            
            # CHECK IF STUDENT IS ALREADY IN DATABASE, IF SO, READ THE UNITS
            with open(filePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # IF 1ST ROW OR AN EMPTY LINE, SKIP
                    if((len(row) == 0) or (row[0] == "Admission number")):
                        continue
                
                    student_admission_number = int(row[0])    
                    
                    # IF ADMISSION NUMBERS ARE SIMILAR, READ THE UNITS
                    if(student_admission_number == admission_number):
                        print(f"Data exists in database, attempting to read {admission_number}'s units...")

                        # GET THE STUDENT UNITS FROM THE ROW, AND CHECK WHETHER DELIMIER IS PRESENT
                        student_recorded_units = row[2]
                        
                        if(student_recorded_units.find("; ")):
                            student_recorded_units = student_recorded_units.split("; ")
                        else:
                            student_recorded_units = [student_recorded_units]
                        
                        # SHOW RECORDED UNITS
                        print(f"\n{student_admission_number}'s recorded units are as follows: ")

                        for _ in range(len(student_recorded_units)):
                            # GETTING THE UNIT NAME AND UNIT MARK OF EACH STUDENT
                            [unit_name_dict, unit_mark_dict] = student_recorded_units[_].split(", ")
                            unit_name = unit_name_dict.split(": ")[1]
                            unit_mark = float(unit_mark_dict.split(": ")[1].replace('}', ''))
                            
                            # CREATE A UNIT DICTIONARY AND APPEND IT TO THE RECORDED UNITS LIST
                            unit = {
                                "unit_name": unit_name, 
                                "unit_mark": unit_mark
                            }

                            recorded_units.append(unit)

                            # SHOW OUTPUT OF RECORDED DATA, AND RETURN THE LIST
                            print(f"\t{_+1}. {unit_name}: {unit_mark:,.2f}")
                        
                        # RETURN LIST OF RECORDRD UNITS AFTER LOOPING THROUGHT THE DATA
                        return recorded_units
        else:
            print(f"\n\tError: {fileName} not found 😞\n")
            return
            
    # A FUNCTION TO GENERATE A RANDOM STUDENT, READ STUDENT'S DATA AND UNITS AND RETURN A STUDENT
    @classmethod
    def get_random_student_data(cls, studentFileName, unitsFileName):
        # CHECK IF THE PARAMETERS ARE OKAY
            # STUDENTFILENAME
        if(type(studentFileName) != type("studentFileName")):
            raise TypeError(f"The student file name, {studentFileName}, must be a string")
        elif(studentFileName == ""):
            raise ValueError("The student file name, 1st parameter, must have a value")
        
            # UNITSFILENAME
        if(type(unitsFileName) != type("unitsFileName")):
            raise TypeError(f"The units file name, {unitsFileName}, must be a string")
        elif(unitsFileName == ""):
            raise ValueError("The units file name, 2nd parameter, must have a value")
        
        # CHECK IF PATH TO FILE TO READ FROM EXISTS, IF SO, GENERATE A RANDOM ADMISSION NUMBER, IF NOT, RAISE ERROR
        print("\nChecking if the student file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        studentFilePath = os.path.join(folderPath, studentFileName)

        if(os.path.exists(studentFilePath)):
            print("File exists, generating a random admission number...")
            # A LIST CONTAINING THE RECORDED ADMISSION NUMBERS
            recorded_admission_numbers = []
            
            # POPULATING THE RECORDED ADMISSION NUMBERS LIST
            with open(studentFilePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # IF 1ST ROW OR AN EMPTY LINE, SKIP
                    if((len(row) == 0) or (row[0] == "Admission number")):
                        continue
                
                    student_admission_number = int(row[0])
                    recorded_admission_numbers.append(student_admission_number)

            print(f"Found {len(recorded_admission_numbers)} possible admission numbers to choose from, picking a random one...")

            # CHECKING IF THE LIST OF ADMISSION NUMBERS HAS A VALUE, IF SO, PICK A RANDOM ONE, IF NOT THROW AN ERROR
            if(len(recorded_admission_numbers) == 0):
                print("\n\tSorry, no student found, consider adding one then trying again\t")
                return
            else:
                random.shuffle(recorded_admission_numbers)
                random_admission_number = recorded_admission_numbers[0]
                
                # READING DATA AND RETURNING A STUDENT
                print(f"Random admission number {random_admission_number} picked, reading the student data...")
                student = cls.get_admitted_student_data(studentFileName, random_admission_number)
                student["recorded_units"] = cls.get_admitted_student_units(unitsFileName, random_admission_number)
                
                # RETURNING CORE STUDENT DATA
                return student
        else:
            print(f"\n\tError: {studentFileName} not found 😞\n")
    
    # A FUNCTION TO READ ALL STUDENTS FROM A FILE AND RETURN AN ARRAY OF EACH STUDENT'S DATA
    @classmethod
    def get_all_student_data(cls, fileName):
       # CHECK IF THE PARAMETERS ARE OKAY
            # FILENAME
        if(type(fileName) != type("fileName")):
            raise TypeError(f"The file name, {fileName}, must be a string")
        elif(fileName == ""):
            raise ValueError("The file name, 1st parameter, must have a value")
        
        # CHECK IF PATH TO FILE TO READ FROM EXISTS, IF SO, READ THE DATA, IF NOT, RAISE ERROR
        print("\nChecking if the student file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        filePath = os.path.join(folderPath, fileName)

        if(os.path.exists(filePath)):
            print("File exists, reading all students' data...\n\nAll the students' general data is as follows...")
            # A LIST CONTAINING THE RECORDED STUDENTS AND THEIR DATA
            recorded_students = []
            
            # READ ALL THE DATA FROM THE FILE
            with open(filePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # IF EMPTY LINE, SKIP
                    if(len(row) == 0):
                        continue
                    
                    [student_admission_number, student_name, student_age, student_total_units, student_total_mark, student_average_mark, student_average_grade] = row

                    # SHOW EACH LINE OF CREDIBLE DATA
                    print(f"\t{student_admission_number}, {student_name}, {student_age}, {student_total_units}, {student_total_mark}, {student_average_mark}, {student_average_grade}")
                    
                    # CREATE A STUDENT INSTANCE FROM EACH LINE AND APPEND IT TO THE LIST
                        # IF 1ST ROW, SKIP
                    if(student_admission_number == "Admission number"):
                        continue
                    else:
                        student = {
                            "admission_number": int(student_admission_number),
                            "name": student_name,
                            "age": int(student_age),
                            "total_units": int(student_total_units),
                            "total_mark": float(student_total_mark),
                            "average_mark": float(student_average_mark),
                            "average_grade": student_average_grade,
                        }
                        
                        recorded_students.append(student)
                
                # RETURN THE LIST OF STUDENTS
                return recorded_students
        else:
            print(f"\n\tError: {fileName} not found 😞\n")
            return 
    
    # A FUNCTION TO READ ALL STUDENTS UNITS FROM A FILE AND RETURN AN ARRAY OF EACH STUDENT'S UNITS
    @classmethod
    def get_all_student_units(cls, fileName):
       # CHECK IF THE PARAMETERS ARE OKAY
            # FILENAME
        if(type(fileName) != type("fileName")):
            raise TypeError(f"The file name, {fileName}, must be a string")
        elif(fileName == ""):
            raise ValueError("The file name, 1st parameter, must have a value")
        
        # CHECK IF PATH TO SUBSEQUENT FILE TO READ FROM EXISTS, IF SO, READ THE DATA, IF NOT, RAISE ERROR
        print("\nChecking if the student units file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        filePath = os.path.join(folderPath, fileName)

        if(os.path.exists(filePath)):
            print("File exists, reading all students' units...\n\nAll the students' units are as follows...")
            # A LIST CONTAINING THE RECORDED STUDENTS AND THEIR UNITS
            recorded_students = []
            
            # READ ALL THE DATA FROM THE FILE
            with open(filePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # A LIST CONTAINING THE RECORDED UNITS
                    recorded_units = []
                    
                    # IF EMPTY LINE, SKIP
                    if(len(row) == 0):
                        continue
                    
                    [student_admission_number, space_tab, student_recorded_units] = row

                    # SHOW EACH LINE OF CREDIBLE DATA
                    print(f"\t{student_admission_number}, {space_tab}, {student_recorded_units}")
                    
                    # CREATE A UNIT INSTANCE FROM EACH LINE AND APPEND IT TO THE STUDENT
                        # IF 1ST ROW, SKIP
                    if(student_admission_number == "Admission number"):
                        continue
                    
                    # CRETE A LIST OF UNITS FROM THE RECORDED UNITS STRING, IN STRING FORMAT
                    if(student_recorded_units.find("; ")):
                        student_recorded_units = student_recorded_units.split("; ")
                    else:
                        student_recorded_units = [student_recorded_units]

                    # CREATING A DICT OF A STUDENT FROM EACH ROW
                    for _ in range(len(student_recorded_units)):
                        # GETTING THE UNIT NAME AND UNIT MARK OF EACH STUDENT
                        [unit_name_dict, unit_mark_dict] = student_recorded_units[_].split(", ")
                        unit_name = unit_name_dict.split(": ")[1]
                        unit_mark = float(unit_mark_dict.split(": ")[1].replace('}', ''))
                        
                        # CREATE A UNIT DICTIONARY AND APPEND IT TO THE STUDENT DICT
                        unit = {
                            "unit_name": unit_name, 
                            "unit_mark": unit_mark
                        }

                        recorded_units.append(unit)
                    
                    # APPENDING THE LIST TO THE STUDENT
                    student = {
                        "admission_number": int(student_admission_number),
                        "recorded_units": recorded_students
                    }
                    
                    recorded_students.append(student)
                
                # RETURN THE LIST OF STUDENTS
                return recorded_students         
        else:
            print(f"\n\tError: {fileName} not found 😞\n")
            return 
    
    # A FUNCTION TO UPDATE STUDENT DATA FROM A FILE
    @classmethod
    def update_student_data(cls, fileName, student):
        # CHECKING IF PARAMETER VALUES ARE OK
            # FILENAME
        if(type(fileName) != type("fileName")):
            raise TypeError(f"The file name, {fileName}, must be a string")
        elif(fileName == ""):
            raise ValueError("The file name, 1st parameter, must have a value")
        
        # CHECK IF FOLDER TO FILE EXISTS, IF SO, CHECK IF STUDENT EXISTS IN DATABASE, IF NOT, RAISE AN ERROR
        print("\nChecking if the folder to student file exists...")
        folderPath = os.path.join(os.path.dirname(__file__), '..', 'records')
        filePath = os.path.join(folderPath, fileName)

        if(os.path.exists(filePath)):
            print(f"Folder and file exists, checking if {student._admission_number}'s data is already in database...")
            # A LIST CONTAINING THE RECORDED STUDENTS DATA
            recorded_data = []
            
            # APPEND THE DATA TO LIST
            with open(filePath, "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    # IF 1ST ROW OR AN EMPTY LINE, SKIP, ELSE ADD TO LIST THE DATA ROW
                    if((len(row) == 0)):
                        continue
                    else:
                        recorded_data.append(row)
                        
            # REWRITE FILE WITH A ROW OF TITLES
            with open(filePath, "w", newline="") as file:
                writer = csv.writer(file)
                row_titles = recorded_data[0]
                writer.writerow(row_titles)
            
            # PARSE THROUGH THE RECORDED DATA FOR THE DATA OF THE REQUIRED STUDENT, AND UPDATE IT
            with open(filePath, "a", newline="") as file:
                writer = csv.writer(file)
                
                for row_of_data in recorded_data[1::]:
                    # CHECK IF ADMISSION NUMBERS ARE SIMILAR, IF SO, AMEND THE DATA, IF NOT, ADD DATA AS IS
                    student_admission_number = int(row_of_data[0])
                    
                    if(student_admission_number == student._admission_number):
                        row_of_data = [student._admission_number, student._name, student._age, student._total_units, student.total_mark, student.average_mark, student.average_grade]
                        
                    writer.writerow(row_of_data)
                
                print(f"{student._name}'s data updated successfully...\n")
            
            # PRINT THE NEW DATA
            print(f"\n{student._admission_number}'s new data is as follows...")
            print(f"\n\tStudent details: \n\t\t[\n\t\t\tStudent name: {student._name},\n\t\t\tStudent Age: {student._age},\n\t\t\tStudent Total Units: {student._total_units},\n\t\t]\n")

            # SHOW TOTAL AND AVERAGE MARK
            print(f"\t\t-> {student._name}'s total mark obtained from the {student._total_units} units is: {float(student.total_mark):,.2f}")
            print(f"\t\t-> {student._name}'s average mark obtained from the {float(student.total_mark):,.2f} total mark is: {float(student.average_mark):,.2f}\n")

            # SHOW AVERAGE GRADE
            print(f"\t\t-> {student._name}'s average grade from an average mark of {float(student.average_mark):,.2f} is: {student.average_grade}\n")
        else:
            print(f"\n\tError: {fileName} not found 😞\n")
            return
            
    # A FUNCTION TO UPDATE STUDENT UNITS FROM A FILE

    # A FUNCTION TO DELETE DATA FROM THE FILE
    