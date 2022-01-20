import re

def validate_required_fields(data,fields):
     errors = []
     for field in fields:
          if data.__contains__(field) != True:
               errors.append(field)

     if errors:
          raise Exception("No ({}) fields found".format(", ".join(errors)))


def validate_required_data(data, fields):
     errors = []
     for field in fields:
          if data[field] == None or data[field] == "":
               errors.append(field)

     if errors:
          raise Exception("Fields ({}) requires data, null value found".format(", ".join(errors)))


def validate_phonenum(num) -> str:
     valid_num = ''
     is_valid = re.search("^9[0-9]{9}$", num)
     if is_valid:
          print("Valid")
          valid_num = "+63"+num
     else:
          return False

     return True