from tabulate import tabulate
from DatabaseInteractor.DAO.StudentDAO import StudentDAO
from DatabaseInteractor.DAO.student_borrowDAO import borrowDAO
from DatabaseInteractor.DTO.StudentDTO import StudentDTO
from DatabaseInteractor.DTO.BorrowDTO import BorrowDTO
from Orchasetrator.BookManager import BookManager

from datetime import date

from Orchasetrator.BorrowUtil import BorrowUtil


class StudentManager:
    # StudentManager Class deals with all the operations related to student
    def __init__(self):
        self.borrowDAO = borrowDAO()
        self.studentDAO = StudentDAO()
        self.borrowUtil = BorrowUtil()
        self.bookManager = BookManager()

# To register new students. Adds student details to the database
    def register_student(self):
        try:
            studentDTO = self.get_student_details_console()
            #print("calling student DAO")
            self.studentDAO.insert_student_details(studentDTO)
            print("Registered student "
                  "successfully")
        except Exception as e:
            raise e

# Method to get the user input and pass them to calling function as DTO
    def get_student_details_console(self):
        try:

            name = input("Name: ")
            Id = int(input("Id: "))
            gender = input("Gender(M/F) : ")
            dept = input("Department: ")
            contact = input("Contact number: ")
            lib_id = input("Library Id: ")
            studentDTO = StudentDTO(Id, name, gender, dept, contact,lib_id)
            print("StudentDTO inside the student Manager", studentDTO)
            return studentDTO
        except Exception as e:
            print(e)

#Method to grant book to the student. It checks the eligibility criteria of the book to be granted and updates the details to database



    def grant_book(self, req_book_id, student_id):
        borrowDTO = BorrowDTO(student_id, req_book_id, date.today(), "0")
        flag = 0
        book_type = self.borrowUtil.get_book_type(req_book_id)

        return_status = self.borrowUtil.get_return_status(req_book_id)

        borrow_count_stu = self.borrowUtil.borrow_limit_stu(student_id)


        try:
            if 'r' in book_type[-1] or return_status is 1:
                    print("book is not available for borrow")
                    return
            else:
                if borrow_count_stu > 4:  # checking the student borrow limit. Max limit : 4
                    print(" Borrow limit reached")
                    return
                else:

                   # print("limit not reached")
                    self.borrowDAO.insert_student__borrow_details(borrowDTO)
                    print("Succesfully updated the details")

        except Exception as e:
                raise e

# to return the book. takes the student Id, Book id and updates the database accordingly
    def return_book(self):
        try:
            stu_id = input("please enter the student Id: ")
            return_id = input("please Enter the book id: ")
            self.borrowDAO.stu_return_book(stu_id, return_id)
            print("successfully updated the details")
        except Exception as e:
            raise e


#Displays details of all the students
    def show_all_students(self):
        try:
            rows = self.studentDAO.show_students()

            headers = ["ID", "Name", "Gender", "Dept", "Contact","lib_id"]
            print(tabulate(rows, headers, "grid"))
        except Exception as e:
            print(e)


# Displays borrow history of the given student
    def show_records_by_id(self):

        try:
            stu_id = int(input("Enter the Student Id: "))
            data = self.borrowDAO.stu_show_records(stu_id)
            headers = ["ID", "Title", "Issued on", "Return Status"]
            print(tabulate(data, headers, "grid"))

        except Exception as e:
            print(e)