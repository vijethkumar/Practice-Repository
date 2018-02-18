class employee:
    salary_raise = 1.05
    num_of_emps = 0
    def __init__(self, fname: object, lname: object, pay: object) -> object:
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.email = fname + '.' + lname +'@amazon.com'
        employee.num_of_emps +=1
    def fullname(self):
        # return self.fname + ' ' + self.lname
        return '{} {}' .format(self.fname,self.lname)
    def raise_salary(self):
        self.pay=int(self.pay * self.salary_raise)

emp1 = employee('vijeth','kumar',1000000)
emp2 = employee('Sindhu','Vijeth',10000000)

# emp1.email = "vijeth.kumar@gmail.com"
print(emp1.fullname())
print(emp2.fullname())
emp1.raise_salary()
print(emp1.pay)
print(employee.fullname(emp1))
print(emp1.__dict__)
print(emp1.salary_raise)
print(employee.__dict__)
print(employee.num_of_emps)

