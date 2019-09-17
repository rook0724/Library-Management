import re

class reValidation():
    studentID = re.compile(r'^\d{3}$')
    teacherID = re.compile(r'^\d{4}$')
    bookID = re.compile(r'^\d{5}$')
    Mobile = re.compile('^[6-9]$|^[0-9]\d{9}$')
    name_valid = re.compile('^[a-zA-z]+([\s]*[a-zA-Z]+)+$')
    type = re.compile(r'^[rR]|[vV]{1}$')
    def validation(self, x, password):
        a = re.search(x, password)
        if a == None:
            flag = 1
        else:
            flag = 0
        return flag

    def bookDTO_validation(self, id,name,author,type,dept):
        try:
            b_id = re.search(self.bookID,id)
            b_name = re.search(self.name_valid, name)
            b_auth = re.search(self.name_valid, author)
            b_type = re.search(self.type,type)
            b_dept = re.search(self.name_valid,dept)

            if b_id == None:
                print("Invalid Id, please try again!")
                return
            elif b_name == None:
                print("Invalid name, please try again!")
                return
            elif b_auth == None:
                print("Invalid name, please try again!")
                return
            elif b_type == None:
                print("Invalid name, please try again!")
                return
            elif b_dept == None:
                print("Invalid name, please try again!")
                return
            else:
                flag = 1
        except Exception as e:
            raise(e)

        return flag



