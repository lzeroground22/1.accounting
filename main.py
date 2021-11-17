from application import salary
from application.db import people
from datetime import datetime, date, time

current_time = datetime.now()

if __name__ == '__main__':
    print('Now is: ', current_time)
    print("salary.py says: ")
    salary.calculate_salary()
    print(" people.py says: ")
    people.get_employees()
