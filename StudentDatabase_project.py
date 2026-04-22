class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls,student):
        cls.student_list.append(student)

class Student:
    def __init__(self,student_id,name,depertment,is_enrolled = False):
        self.__student_id = student_id
        self.__name = name
        self.__depertment = depertment
        self.__is_enrolled = is_enrolled
        StudentDatabase.add_student(self)

    @property
    def student_id(self):
        return self.__student_id
    @property
    def name(self):
        return self.__name
    @property
    def depertment(self):
        return self.__depertment
    @property
    def is_enrolled(self):
        return self.__is_enrolled
    
    def enroll_student(self):
        if self.__is_enrolled == False:
            self.__is_enrolled = True
            print(f"'{self.__name}' has been successfully enrolled.")
        else:
            print(f"'{self.__name}' is already enrolled")
    def drop_student(self):
        if self.__is_enrolled == True:
            self.__is_enrolled = False
            print(f"'{self.__name}' has been dropped")
        else:
            print(f"'{self.__name}' is not currently enrolled")
    def view_student_info(self):
        if self.__is_enrolled == True:
            print(f"""---------------------
Student id : {self.__student_id}
Name       : {self.__name}
Depertment : {self.__depertment}
Status     : Enrolled
-----------------------""")
        else:
            print(f"""---------------------
Student id : {self.__student_id}
Name       : {self.__name}
Depertment : {self.__depertment}
Status     : Not Enrolled
-----------------------""")
            
    def __repr__(self):
        return f"Student Id : {self.__student_id}, Name: {self.__name}"

s1 = Student(1, "Thasin", "CSE")
s2 = Student(2, "Lam",    "EEE")
s3 = Student(3, "Rafi",   "BBA")

def find_stu(st_id):
    for st in StudentDatabase.student_list:
        if st.student_id == st_id:
            return st
    return None

def menu():
    while True:
        print("""------------------------
    Student Database
-------------------------
              
1.View all Students
2.Enroll Student
3.Drop Student
4.Exit
-------------------------""")
        choice = input("Enter your choice(1-4): ").strip()
        if choice =='1':
            print("\n    ---All Student---")
            for st in StudentDatabase.student_list:
                st.view_student_info()

        elif choice =='2':
            give = int(input("Enter a student id : "))
            st = find_stu(give)
            if st is None:
                print("Student Id not found")
            else:
                st.enroll_student()
        elif choice =='3':
            give = int(input("Enter a student id : "))
            st = find_stu(give)
            if st is None:
                print("Student Id not found")
            else:
                st.drop_student()
        elif choice == '4':
            print("Thanks good bye")
            break
        else:
            print("Invalid choice. please try again")


menu()
    

    

        

    
    