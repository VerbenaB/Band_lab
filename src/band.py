class Band:
    def __init__(self, name, guitarist, singer, bassist, manager):
        self.name = name
        self.musicians = [guitarist, singer, bassist]
        self.manager = manager

    def calculate_payroll(self):
        return self.manager.calculate_payroll(self.musicians)

    def pay_salaries(self):
        return self.manager.pay_salaries(self.musicians)

    def play(self):
        full_string = ""
        for musician in self.musicians:
            full_string += musician.play() + "/n"
        return full_string
        

