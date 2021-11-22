from application.salary import *
from application.db.people import *
from datetime import datetime

current_time = datetime.now()

if __name__ == '__main__':
    print('Now is: ', current_time)

    print("salary.py says: ")
    calculate_salary()

    print(" people.py says: ")
    get_employees()
