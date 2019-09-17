
from Orchasetrator.BookManager import BookManager
from Orchasetrator.StudentManager import StudentManager
from Orchasetrator.TeacherManager import TeacherManager


class LibraryAssistant:
    def __init__(self):
        self.student_manager = StudentManager()
        self.book_manager = BookManager()
        self.teacher_manager = TeacherManager()


    def invoke_student_manager(self):

        while True:
            opt = input("Please enter the choice: \n1.Register\n2.Request book\n3.Return book\n4.Show Records_by_id \n5. Show Student records\n6.Exit")
            if opt == "1":
                try:
                    self.student_manager.register_student()
                except Exception as e:
                    print(e)
            elif opt =='2':
                try:
                    stu_id = input("please enter the student id: ")
                    req_bid = input("Please enter the book id: ")
                    self.student_manager.grant_book(req_bid,stu_id)
                except Exception as e:
                    print(e)
            elif opt == '3':
                try:
                    self.student_manager.return_book()
                except Exception as e:
                    print(e)
            elif opt =='4':
                try:
                    self.student_manager.show_records_by_id()
                except Exception as e:
                    print(e)
            elif opt =='5':
                try:
                    self.student_manager.show_all_students()
                except Exception as e:
                    print(e)
            elif opt == '6':
                exit()

    def invoke_teacher_manager(self):

        while True:
            opt = input("Please enter the choice: \n1.Register\n2.Request book\n3.Return book\n4.Show Records_by_id \n5. Show Student records\n6.Exit")
            if opt == "1":
                try:
                    self.teacher_manager.register_student()
                except Exception as e:
                    print(e)
            elif opt =='2':
                try:
                    teach_id = input("please enter the student id: ")
                    req_bid = input("Please enter the book id: ")
                    self.teacher_manager.grant_book(req_bid,teach_id)
                except Exception as e:
                    print(e)
            elif opt == '3':
                try:
                    self.teacher_manager.return_book()
                except Exception as e:
                    print(e)
            elif opt =='4':
                try:
                    self.teacher_manager.show_teach_records_by_id()
                except Exception as e:
                    print(e)
            elif opt =='5':
                try:
                    self.teacher_manager.show_all_teachers()
                except Exception as e:
                    print(e)
            elif opt == '6':
                exit()

    def invoke_book_manager(self):
            while True:

                book_opt = input("Please enter the choice: \n1.Add Book \n2.Delete Book \n3.Show all Books \n4.Show Book by ID \n5.Exit")
                if book_opt =="1":
                    try:
                        self.book_manager.register_book()
                    except Exception as e:
                        print(e)
                elif book_opt == '2':
                    try:
                        Id = int(input("Enter the Book Id: "))
                        self.book_manager.delete_book(Id)
                    except Exception as e:
                        print(e)

                elif book_opt == '3':
                    try:
                        print("calling show all books")
                        self.book_manager.show_all_books()
                    except Exception as e:
                        print(e)
                elif book_opt == '4':
                    b_id = input("Please enter the book Id: ")
                    try:
                        self.book_manager.show_book_id(b_id)
                    except Exception as e:
                        print(e)
                elif book_opt == '5':
                    exit()


if __name__ == "__main__":
    library_assistant = LibraryAssistant()
    option = input("Please select your choice : \n1.Book Management \n2.Student Management\n3.Teacher Management\n4. Exit\n")
    print(option)
    if option == "1":
        try:
            library_assistant.invoke_book_manager()
        except Exception as e:
            raise e
    elif option == "2":
        try:
            library_assistant.invoke_student_manager()
        except Exception as e:
            raise e
    elif option == "3":
        try:
            library_assistant.invoke_teacher_manager()
        except Exception as e:
            raise e
    elif option == "4":
        exit()





