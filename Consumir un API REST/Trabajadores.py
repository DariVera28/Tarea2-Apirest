import requests

url = "https://dummy.restapiexample.com/api/v1/employees"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    employees = data["data"]

    total_employees = len(employees)

    total_salary = sum(float(employee["employee_salary"]) for employee in employees)
    average_salary = total_salary / total_employees

    total_age = sum(int(employee["employee_age"]) for employee in employees)
    average_age = total_age / total_employees

    salaries = [float(employee["employee_salary"]) for employee in employees]
    min_salary = min(salaries)
    max_salary = max(salaries)

    ages = [int(employee["employee_age"]) for employee in employees]
    min_age = min(ages)
    max_age = max(ages)

    print(f"Número total de empleados: {total_employees}")
    print(f"Promedio de salario: {average_salary}")
    print(f"Promedio de edad: {average_age}")
    print(f"Salario mínimo: {min_salary}")
    print(f"Salario máximo: {max_salary}")
    print(f"Edad mínima: {min_age}")
    print(f"Edad máxima: {max_age}")

else:
    print(f"Error al hacer la solicitud. Código de estado: {response.status_code}")

