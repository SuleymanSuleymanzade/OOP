class PaymentSystem:
    def __init__(self, employees):
        self.__employees = employees 

    def show_salaries(self):
        for employee in self.__employees:
            print(f"The salary of {employee}: {employee.salary}")
    def add_employee(self, employee):
        self.__employees.append(emplyee)

    def remove_empoyee(self, employee):
        self.__employees.remove(employee)

class Employee:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

class SalaryEmployee(Employee):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname)
        self._salary = salary
 
    def __str__(self):
        return f"{self._name} {self._surname}"
   
    @property
    def salary(self):
        return self._salary 

    @salary.setter
    def salary(self, sal):
        self._salary = sal 

class HourlyEmployee(Employee):
    def __init__(self, name, surname, hours, salary_rate):
        super().__init__(name, surname)
        self._hours = hours
        self._salary_rate = salary_rate 


    def __str__(self):
        return f"{self._name} {self._surname}"
 
    @property
    def salary(self):
        return self._salary_rate * self._hours 

    @salary.setter
    def hours_rate(self, hours, rate):
        self._hours = hours
        self._salary_rate = rate

class CommissionEmployee(Employee):
    def __init__(self, name, surname, salary, commission):
        super().__init__(name, surname)
        self._salary = salary
        self._commission = commission 

    def __str__(self):
        return f"{self._name} {self._surname}"
 

    @property
    def salary(self):
        return self._salary + self._commission

    
    @salary.setter
    def salary_commission(self, salary, commission):
        self._salary = salary
        self._commission = commission 


