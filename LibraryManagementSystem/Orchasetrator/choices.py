class choices:
    def librarian_choice(self, option):
        lib_op = input("How can I can help you? 1. Book Management \n.2 Student Management \n.3 Teacher Management \n.4. Exit")
        if lib_op == 1:
            try:
                library_assistant.invoke_book_manager()
            except Exception as e:
                raise e
        elif lib_op == 2:
            try:
                library_assistant.invoke_student_manager()
            except  Exception as e:
                raise e

        elif lib_op == 3:
            try:
                library_assistant.invoke_teacher_manager()
            except Exception as e:
                raise e
        elif lib_op == 4:
            exit()
    def student_choice(self):