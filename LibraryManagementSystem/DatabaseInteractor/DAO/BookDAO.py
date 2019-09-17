from DatabaseInteractor.DatabseUtil import DataBaseUtil
from DatabaseInteractor.QueryConstants import queries


class BookDAO:
    def __init__(self):
        self.db_object = DataBaseUtil()

    def insert_book_details(self, bookDTO):
        db_connection = self.db_object.get_data_base_connection()
        try:
            sql_query = queries.insert_into_book % (bookDTO.b_id, bookDTO.b_title,bookDTO.b_author,bookDTO.b_type,bookDTO.b_dept)
            print(sql_query)
            cursor = db_connection.cursor()
            cursor.execute(sql_query)
            db_connection.commit()
        except Exception as e:
            raise e
        finally:
            self.db_object.close_data_base_connection(db_connection)


    def delete_book_id(self,id):

        try:
            sql_query = queries.delete_book_record % id
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data


    def show_books(self):

        try:
            sql_query = queries.show_all_books
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e

        return data

    def show_book_id_stu(self,id):

        try:
            sql_query = queries.show_book_id_stu % (id)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e

        return data

    def show_book_id_teach(self,id):

        try:
            sql_query = queries.show_book_id_teach % (id)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data





    def book_check(self,id):
        try:
            sql_query = queries.get_book_id % (id)
            data = self.db_object.execute_command(sql_query)
        except Exception as e:
            raise e
        return data


