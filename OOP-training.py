class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10
    def __init__(self, first, last, pay, pro_lang): # Eme le kateka eger btewe nrxek zyad bkey bo class e koneke le regey class y tazewe.
        super().__init__(first, last, pay) # be super() peman wt ke ew 3 nrxey class y peshw ke Employee byhene
        self.pro_lang = pro_lang # Ew nrxey ke demanewet zyady bkeyn be asayy wek class ekany tr aynasenyn.

class Manager(Employee): #heman instance kany class y developer dehenyn legell ewey demanewet zyay bkeyn
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print('---> ', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, "python")
dev_2 = Developer('Test', 'Employee', 60000, "Java" )

print(dev_1.email)
print(dev_2.email)
print(dev_1.pay) # Lere nrxeke nagorret
dev_1.apply_raise()
print(dev_1.pay) # lere nrxeke gorra chwnke apply condition ynweman krdwe.
print(dev_1.pro_lang)

manager1 = Manager("Sue", "Adam", 90000, [dev_1])

print(manager1.email)
manager1.add_emp(dev_2)
manager1.print_emp()
# Bo ewey bzany ke ch beshek instance y besheky tre
print("-" * 10)
print(isinstance(manager1, Manager))
print(isinstance(dev_1, Manager))
print(isinstance(manager1, Developer))
print(isinstance(manager1, Employee))
# bo ewey bzany kame subclass y kameye
print("-" * 10)

print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))
print(issubclass(Employee, Developer))
print(issubclass(Employee, Manager))




