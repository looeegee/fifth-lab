from datetime import date, datetime
from exercise.model import User

class UserController:
    def __init__(self):
        self.users=[]
    def create_user(self, name, last_name, address, gender, birth_date, start_date=date.today()):
        u=User(name, last_name, address, gender, birth_date)
        self.users.append(u)
    def print_users(self):
        for user in self.users:
            print(user)

m="male"
f="female"
gender= m or f
add1=("80-142", "S.George st.", 20)
add2=("80-142", "S.George st.", 18)
add3=("80-141", "King's Hill st.", 15)
add4=("80-140", "Miracles square", 2)
add5=("80-143", "S.John st.", 142)
uc=UserController()
uc.create_user("Alex", "Johnsson", add1, m, date(2000, 2, 2))
uc.create_user("Concetta", "Arnold", add2, f, date(1996, 3, 20))
uc.create_user("Assunta", "Smith", add3, f, date(2001, 11, 25))
uc.create_user("Ciro", "Gustavson", add4, m, date(1993, 5, 12))
uc.create_user("Gennaro", "Sturridge", add5, m, date(1999, 8, 30))
uc.print_users()