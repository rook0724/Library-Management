from DatabaseInteractor.DAO.BookDAO import BookDAO
from DatabaseInteractor.DAO.student_borrowDAO import borrowDAO
from DatabaseInteractor.DTO.BookDTO import BookDTO

from tabulate import tabulate


from Orchasetrator.Validations import reValidation


class BookManager:
    def __init__(self):
        self.borrowDAO = borrowDAO()
        self.bookDAO = BookDAO()
        self.re_validate = reValidation()


    def register_book(self):
        try:
            BookDTO = self.get_book_details_console()
            #print("calling student DAO")
            self.bookDAO.insert_book_details(BookDTO)
            print("Registered student "
                  "successfully")
        except Exception as e:
            raise e

    def get_book_details_console(self):
        try:
            flag = 0
            name = input("Enter the Book name: ")
            Id = input("Enter the Book Id: ")
            author = input("Please enter the Author name: ?")
            type = input("Enter the gender (R/V) : ")
            dept = input("Please enter the department: ")
            flag=self.re_validate.bookDTO_validation(Id,name,author,type,dept)
            if flag ==1:
                print("Validations succesful")
                bookDTO = BookDTO(Id, name, author, type, dept)
                return bookDTO

        except Exception as e:
            print(e)


    def delete_book(self,Id):
        x=0
        flag_stu = 0

        try:

            rows_stu = self.bookDAO.show_book_id_stu(Id)
            rows_teach = self.bookDAO.show_book_id_teach(Id)
            flag_stu,stu_id = self.delete_book_check(rows_stu)
            flag_teach, teach_id = self.delete_book_check(rows_teach)

            if flag_stu == 0 and flag_teach == 0:
                print("Book can be deleted")

                self.bookDAO.delete_book_id(Id)

            elif(flag_stu !=0):
                print("Book can't be deleted, it is borrowed by teacher:", stu_id,"\nPlease try again, once they return the book" )
            else:
                print("Book can't be deleted, it is borrowed by teacher:", teach_id,"\nPlease try again, once they return the book" )
        except Exception as e:
            print(e)

    def show_all_books(self):
        try:
            rows = self.bookDAO.show_books()
            headers = ["ID", "Title", "Author","Type", "Dept"]
            print(tabulate(rows, headers, "grid"))
        except Exception as e:
            print(e)

    def show_book_id(self,id):
        try:
            rows_stu  = self.bookDAO.show_book_id_stu(id)
            rows_teach = self.bookDAO.show_book_id_teach(id)
            headers = ["ID", "Date", "Return Status"]
            rows_book = self.bookDAO.book_check(id)
            if len(rows_book)==0:
                print("Invalid Book ID")
            else:
                if len(rows_stu) == 0 and len(rows_teach) == 0:
                    print("Book was never borrowed")
                else:
                    print("Following Teacher have borrowed this book",id, "so far:")
                    print(tabulate(rows_teach, headers, "grid"))
                    print("Following Teacher have borrowed this book", id, "so far:")
                    print(tabulate(rows_stu, headers, "grid"))
        except Exception as e:
            print(e)

    def delete_book_check(self,data):
        flag = 0
        y=0
        for i in range(0, len(data)):
            x = (data[i][-1])
            if x == 0:
                y = data[i][0]
                flag = 1
        return flag,y

    def status_book_check(self, data):
        flag = 0
        for i in range(0, len(data)):
            if 0 in data:
                flag = 1
        return flag