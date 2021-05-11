

class Manager:
    def __init__(self, name, address="None"):
        self.name = name
        self.address = address

    def pay_salaries(self, musicians):
        for musician in musicians:
            salary = musician.get_salary()
            musician.add_money(salary)

    def calculate_payroll(self, musicians):
        total = 0
        for musician in musicians:
            total += musician.get_salary()
        return total