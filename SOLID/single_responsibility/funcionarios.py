class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Calculate_Tax:
    def calculate_tax(self):
        # calculate tax based on salary
        if self.salary < 1000:
            return self.salary * 0.1
        elif self.salary < 5000:
            return self.salary * 0.2
        else:
            return self.salary * 0.3

class Save_Database:
    def save_to_database(self):
        # save employee data to a database
        print(f"Saving {self.name} to database...")

class Send_Email:
    def send_email(self):
        # send an email to the employee
        print(f"Sending email to {self.name}...")