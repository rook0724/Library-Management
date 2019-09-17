from DatabaseInteractor.DAO.BookDAO import BookDAO
from DatabaseInteractor.DAO.StudentDAO import StudentDAO
from DatabaseInteractor.DAO.student_borrowDAO import borrowDAO


class BorrowUtil:
    def __init__(self):
        self.borrowDAO = borrowDAO()
        self.studentDAO = StudentDAO()
        self.bookDAO = BookDAO()

    def get_book_type(self, req_bid):
        print("get book type invoked")
        try:
            book_type = self.borrowDAO.get_book_type(req_bid)  # retreiving type of the book
            return book_type
        except Exception as e:
            raise e

#cheking Borrow student details
    def borrow_limit_stu(self,stu_id):
        print("invoked borrow_limit_stu")
        try:
            borrow_details_stu = self.borrowDAO.get_stu_borrow_count(stu_id) #student borrow details
            borrow_count_stu = len(borrow_details_stu)
            return borrow_count_stu

        except Exception as e:
            raise e



    def borrow_limit_teach(self,teach_id):
        try:
            borrow_details_teach = self.borrowDAO.get_teach_borrow_count(teach_id)
            borrow_count_teach = len(borrow_details_teach)
            print(borrow_count_teach)
            return borrow_count_teach

        except Exception as e:
            raise(e)

#chek if the book is borrowed by someone else
    def get_return_status(self,req_bid):

        try:
            rows_stu = self.borrowDAO.get_book_status_stu(req_bid)  # retrieiving the student data who has borrowed the book so far
            rows_teach = self.borrowDAO.get_book_status_teach(req_bid)
            if(len(rows_stu) ==0) and (len(rows_teach) == 0) :
                  # If both student and teacher data is empty, good to go. book can be lent .
                flag = 0
                return flag
            elif (len(rows_stu) != 0 ) or (len (rows_teach) != 0):  # if some of the stundents have borrowed:

                flag = 1
                return flag
        except Exception as e:
            raise e

#should be inside the student manager, teach_manager




