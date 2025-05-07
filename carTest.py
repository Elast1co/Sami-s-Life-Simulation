class Person:
    def __init__(self, name, money, mood, health_rate):
        self.name = name
        self.money = money
        self.mood = mood
        self.health_rate = max(0, min(100, health_rate))  

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 75
        elif meals == 1:
            self.health_rate = 50

    def buy(self, items):
        self.money -= items * 10  

class Employee(Person):
    def __init__(self, name, money, mood, health_rate, emp_id, car, email, salary, distance_to_work):
        super().__init__(name, money, mood, health_rate)
        self.emp_id = emp_id
        self.car = car
        self.email = email
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):
        if self.car:
            self.car.run(60, distance)

    def refuel(self, gas_amount=100):
        if self.car:
            self.car.refuel(gas_amount)

    def send_mail(self, to, subject, message):
        print(f"Sending email to {to}\nSubject: {subject}\nMessage: {message}")

class Car:
    def __init__(self, name, fuel_rate, velocity):
        self.name = name
        self.fuel_rate = max(0, min(100, fuel_rate))  
        self.velocity = max(0, min(200, velocity)) 

    def run(self, velocity, distance):
        self.velocity = max(0, min(200, velocity))
        fuel_needed = distance // 10 * 10  
        if self.fuel_rate >= fuel_needed:
            self.fuel_rate -= fuel_needed
            print(f"Car reached the destination with velocity {self.velocity} and remaining fuel {self.fuel_rate}.")
        else:
            self.stop()
            print("Car stopped before reaching the destination due to low fuel.")

    def stop(self):
        self.velocity = 0
        print("Car has stopped.")

    def refuel(self, gas_amount):
        self.fuel_rate = min(100, self.fuel_rate + gas_amount)
        print(f"Car refueled. Current fuel level: {self.fuel_rate}")

class Office:
    employees = []  

    def __init__(self, name):
        self.name = name

    def get_all_employees(self):
        return [emp.name for emp in self.employees]

    def get_employee(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def hire(self, employee):
        self.employees.append(employee)

    def fire(self, emp_id):
        self.employees = [emp for emp in self.employees if emp.emp_id != emp_id]

    @classmethod
    def change_salary(cls, emp_id, new_salary):
        emp = next((emp for emp in cls.employees if emp.emp_id == emp_id), None)
        if emp:
            emp.salary = new_salary

    @staticmethod
    def is_employee_late(time_in, expected_time):
        return time_in > expected_time

    @staticmethod
    def deduct(emp, amount):
        emp.salary -= amount
        print(f"{emp.name}'s salary deducted by {amount}. New salary: {emp.salary}")

    @staticmethod
    def reward(emp, amount):
        emp.salary += amount
        print(f"{emp.name} received a reward of {amount}. New salary: {emp.salary}")


    
car1 = Car("Fiat", 50, 120)
   


print("\nTesting Car run method:")
car1.run(100, 50)
print(f"Fuel after drive: {car1.fuel_rate}")


print("\nTesting Car stopping due to low fuel:")
car1.run(100, 500)
print(f"Fuel after trying to drive long distance: {car1.fuel_rate}")
    

print("\nTesting Car refueling:")
car1.refuel(40)
print(f"Fuel after refueling: {car1.fuel_rate}")

    