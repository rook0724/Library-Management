from DatabaseInteractor.DatabseUtil import DataBaseUtil
from DatabaseInteractor.QueryConstants import queries


class borrowDAO:
    def __init__(self):
        self.db_object = DataBaseUtil()

    def insert_student__borrow_details(self, borrowDTO):
        try:
            sql_query = queries.insert_into_teacher_borrow % (borrowDTO.sb_id, borrowDTO.sb_bid, borrowDTO.sb_date, borrowDTO.sb_return)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e

    def insert_teacher__borrow_details(self, borrowDTO):
        try:
            sql_query = queries.insert_into_teacher_borrow % (
            borrowDTO.sb_id, borrowDTO.sb_bid, borrowDTO.sb_date, borrowDTO.sb_return)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e

    def stu_return_book(self, stu_id, id):
        try:
            sql_query = queries.return_book_stu % (stu_id,id)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e

    def teach_return_book(self, stu_id, id):
        try:
            sql_query = queries.return_book_teach % (stu_id, id)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e

    def stu_show_records(self, student_id):
        try:
            sql_query = queries.show_student_record % student_id
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data

    def teach_show_records(self, student_id):

        try:
            sql_query = queries.show_teacher_record % student_id
            data = self.db_object.execute_command(sql_query)

        except Exception as e:
            raise e
        return data

    def get_book_status_stu(self, b_id):
        try:
            sql_query = queries.borrow_book_status_stu % (b_id)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data

    def get_book_type(self, b_id):
        try:
            sql_query = queries.borrow_book_type % (b_id)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data

    def get_book_status_teach(self, b_id):
        try:
            sql_query = queries.borrow_book_status_teach % b_id
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data

    def get_stu_borrow_count(self, id):
        try:
            sql_query = queries.borrow_student_limit % id
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data

    def get_teach_borrow_count(self, id):
        try:
            sql_query = queries.borrow_teacher_limit % id
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data