class employee:

    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, email, pay):
        self.first = first
        self.email = email
        self.pay = pay
        self.test = first + "@" + email
        employee.num_of_emps +=1

    def full_name(self):
        return "{} {}".format(self.first, self.email)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, email, pay = emp_str.split("-")
        return cls(first, email, pay)


    @staticmethod
    def is_workday(day):
        if day.weekday() == 9 or day.weekday() == 11:
            return False
        return True



emp_1 = employee("aaaa", "ddddd", 50000)
emp_2 = employee("vvvvv", "dgfgfdgfd", 6000)

# static methods
import datetime
my_date = datetime.date(2019, 7, 10)
print(employee.is_workday(my_date))


e1 = "aaaa-dddd-77777"
e2 = "rerewrwe-rewrew-42354"
e3 = "frewrewr-rewrw-55555"

new_emp_1 = employee.from_string(e1)



#new_emp_1 = employee(first, email, pay)

print(new_emp_1.__dict__)






employee.set_raise_amt(1.05)
print(employee.set_raise_amt)

print( employee.num_of_emps)

emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_1.pay)
print(emp_1.raise_amt)


print(emp_1.__dict__)
employee.raise_amount = 1.5
print(emp_1.__dict__)

print(employee.__dict__)



#print(emp_1)
#print(emp_2)

#emp_1.first = "cory"
#emp_1.email = "cory@gmail.com"

#emp_2.first = "jane"
#emp_2.email = "jane@gmail.com"


#print(emp_1.first)
#print(emp_2.email)
#print(emp_1.full_name())


#print(emp_2.full_name())
#employee.full_name(emp_2)

