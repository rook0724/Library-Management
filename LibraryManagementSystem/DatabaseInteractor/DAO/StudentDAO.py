from DatabaseInteractor.DatabseUtil import DataBaseUtil
from DatabaseInteractor.QueryConstants import queries


class StudentDAO:
    def __init__(self):
        self.db_object = DataBaseUtil()

    def insert_student_details(self, studentDTO):
        try:
            sql_query = queries.insert_into_student % (studentDTO.stu_id, studentDTO.stu_name,studentDTO.stu_gender,studentDTO.stu_dept,studentDTO.stu_contact,studentDTO.stu_lib_id)
            self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e

    def show_students(self):
        try:
            sql_query = queries.show_all_students
            rows = self.db_object.execute_command(sql_query)
        except Exception as e:
            print(e)
        return rows