# Sami’s Life Simulation 🧠🚗💼

This project is a Python-based simulation that models the life of a fictional character, **Sami**, using Object-Oriented Programming (OOP) principles. It reflects real-world behavior and interaction between a person, an employee, and a car.

## 📌 Overview

The simulation covers various aspects of Sami’s daily routine such as:

- Sleeping and its effect on mood
- Eating habits and health tracking
- Working hours and emotional response
- Driving to work and fuel management

It uses **OOP principles** to structure and organize the logic efficiently.

## 🧱 Object-Oriented Concepts Applied

- **Encapsulation**: Attributes like `money`, `mood`, `health_rate` are managed within classes.
- **Inheritance**: The `Employee` class inherits from the `Person` class.
- **Method Overriding**: `Employee` extends the behavior of `Person` with additional methods like `work()`, `drive()`, and `refuel()`.
- **Composition**: The `Employee` class uses a `Car` object to model commuting.

## 🧑‍💻 Classes & Methods

- **`Person`**
  - `sleep(hours)`
  - `eat(meals)`
  - `buy(items)`

- **`Employee(Person)`**
  - `work(hours)`
  - `drive(distance)`
  - `refuel(gas_amount=100)`

- **`Car`**
  - `run(fuel_rate, distance)`
  - `refuel(gas_amount)`

## 🔧 Tech Stack

- Language: **Python 3**
- IDE: **Visual Studio Code**
- No external libraries — pure Python OOP practice

## 📁 Project Structure
├── carTest.py
├── empTest.py
├── officeTest.py
└── personTest.py

Each file includes test scenarios to simulate different parts of Sami’s routine.

## 🚀 How to Run

1. Clone the repository
2. Run each test file individually using Python:
   ```bash
   python carTest.py


