from Application.db.people import get_employees
from Application.salary import calculate_salary
from datetime import datetime

def main():
    people = ["Александр", "Иван"]
    print(datetime.now())
    employees = get_employees(people)

    for employee in employees:
        calculate_salary(employee)



if __name__ == '__main__':
    main()
