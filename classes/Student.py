# A CLASS TO GENERATE A PROPER STUDENT
class Student:
    # AN INIT FUNCTION TO GET THE VALUES AS ARGUMENTS
    def __init__(self, admission_number, name, age, total_units):
        self.admission_number = admission_number
        self.name = name
        self.age = age
        self.total_units = total_units

        # CREATING OWN VARIABLES FROM OBTAINED DATA
        self.recorded_units = []
        self.total_mark = 0
        self.average_mark = 0
        self.average_grade = 'N/A'

    # CHECKING IF ADMISSION NUMBER IS A PROPER VALUE
    @property
    def admission_number(self):
        return self._admission_number
    
    @admission_number.setter
    def admission_number(self, value):
        if(type(value) != type(101)):
            raise TypeError(f"The student admission number, {value}, must be an integer")
        elif(value == ""):
            raise ValueError("The student admission number, 1st parameter, must have a value")
        
        self._admission_number = value

    # CHECKING IF NAME IS A PROPER VALUE
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(type(value) != type("value")):
            raise TypeError(f"The student name, {value}, must be a string")
        elif(value == ""):
            raise ValueError("The student name, 2nd parameter, must have a value")
        
        self._name = value

    # CHECKING IF AGE IS A PROPER VALUE
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if(type(value) != type(18)):
            raise TypeError(f"The student age, {value}, must be an integer")
        elif(value < 18):
            raise ValueError("The student age, 3rd parameter, must be 18 and up")
        
        self._age = value

    # CHECKING IF TOTAL UNITS IS A PROPER VALUE
    @property
    def total_units(self):
        return self._total_units
    
    @total_units.setter
    def total_units(self, value):
        if(type(value) != type(1)):
            raise TypeError(f"The student total units, {value}, must be an integer")
        elif(value <= 0):
            raise ValueError("The student total units, 4th parameter, must have a value")
        
        self._total_units = value

    # A FUNCTION TO POPULATE LIST OF RECORDED UNITS
    def populate_recorded_units(self):
        for _ in range(self._total_units):
            # GETTING UNIT DETAILS, WHICH ARE THE NAME AND MARK
            unit_name = ""
            unit_mark = 0

                # UNIT NAME
            while True:
                try:
                    unit_name = input(f"\n\t1. What is the name of unit {_+1}: ").strip().title()

                    if(unit_name == ""):
                        raise ValueError
                except ValueError:
                    print("\n\t\tThe unit name must have a value\n")
                else:
                    break

                # UNIT MARK
            while True:
                try:
                    unit_mark = float(input(f"\t2. What is the mark scored in {unit_name}: "))

                    if(unit_mark < 0):
                        raise ValueError
                except ValueError:
                    print("\n\t\tThe unit mark must be a float value greater than 0\n")
                else:
                    break

            # CREATE A UNIT DICTIONARY AND APPENDIT TO THE RECORDED UNITS LIST
            unit = {
                "unit_name": unit_name, 
                "unit_mark": unit_mark
            }

            self.recorded_units.append(unit)

    # A FUNCTION TO CALCULATE TOTAL MARK FROM RECORDED UNITS'
    def calculate_total_mark(self):
        sum = 0

        for _ in range(self.total_units):
            unit = self.recorded_units[_]
            sum += unit["unit_mark"]

        self.total_mark = sum
            
    # A FUNCTION TO CALCULATE AVERAGE MARK FROM TOTAL MARK
    def calculate_average_mark(self):
        self.average_mark = self.total_mark / self.total_units

    # A FUNCTION TO CALCULATE THE AVERAGE GRADE
    def calculate_average_grade(self):
        # CHECKING IF AVERAGE GRADE IS OK
        if((self.average_mark < 0) or (self.average_mark > 100)):
            raise ValueError(f"The average grade {self.average_grade} is unrealistic")
        
        if(self.average_mark >= 85):
            self.average_grade = 'A'
        elif((self.average_mark < 85) and (self.average_mark >= 80)):
            self.average_grade = 'A-'
        elif((self.average_mark < 80) and (self.average_mark >= 75)):
            self.average_grade = 'B+'
        elif((self.average_mark < 75) and (self.average_mark >= 70)):
            self.average_grade = 'B'
        elif((self.average_mark < 70) and (self.average_mark >= 65)):
            self.average_grade = 'B-'
        elif((self.average_mark < 65) and (self.average_mark >= 60)):
            self.average_grade = 'C+'
        elif((self.average_mark < 60) and (self.average_mark >= 55)):
            self.average_grade = 'C'
        elif((self.average_mark < 55) and (self.average_mark >= 50)):
            self.average_grade = 'C-'
        elif((self.average_mark < 50) and (self.average_mark >= 45)):
            self.average_grade = 'D+'
        elif((self.average_mark < 45) and (self.average_mark >= 40)):
            self.average_grade = 'D'
        elif((self.average_mark < 40) and (self.average_mark >= 35)):
            self.average_grade = 'D-'
        else:
            self.average_grade = 'E'

    # A FUNCTION TO SHOW THE STUDENT DATA
    def get_student_data(self):
        # PRINT GENERAL DATA
        print(f"\nStudent details: \n\t[\n\t\tStudent name: {self._name},\n\t\tStudent Age: {self._age},\n\t\tStudent Total Units: {self._total_units},\n\t]\n")

        # SHOW RECORDED UNITS
        print(f"\t{self._name}'s recorded units are as follows: ")

        for _ in range(self.total_units):
            unit = self.recorded_units[_]

            print(f"\t\t{_+1}. '{unit["unit_name"]}': {unit["unit_mark"]:,.2f}")

        # SHOW TOTAL AND AVERAGE MARK
        print(f"\n\t-> {self._name}'s total mark obtained from the {self.total_units} units is: {self.total_mark:,.2f}")
        print(f"\t-> {self._name}'s average mark obtained from the {self.total_mark:,.2f} total mark is: {self.average_mark:,.2f}\n")

        # SHOW AVERAGE GRADE
        print(f"\t-> {self._name}'s average grade from an average mark of {self.average_mark:,.2f} is: {self.average_grade}\n")
