import requests

# Hacer la solicitud a la API
url = 'https://dummy.restapiexample.com/api/v1/employees'
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()

    # Obtener el número de empleados
    total_employees = len(data['data'])

    # Calcular el promedio de salario de los empleados
    salaries = [employee['employee_salary'] for employee in data['data']]
    average_salary = sum(salaries) / len(salaries)

    # Calcular el promedio de edad de los empleados
    ages = [employee['employee_age'] for employee in data['data']]
    average_age = sum(ages) / len(ages)

    # Encontrar el salario mínimo y máximo
    min_salary = min(salaries)
    max_salary = max(salaries)

    # Encontrar la edad menor y mayor de los empleados
    min_age = min(ages)
    max_age = max(ages)

    # Mostrar los resultados
    print(f"Número total de empleados: {total_employees}")
    print(f"Promedio de salario de los empleados: {average_salary}")
    print(f"Promedio de edad de los empleados: {average_age}")
    print(f"Salario mínimo: {min_salary}")
    print(f"Salario máximo: {max_salary}")
    print(f"Edad menor de los empleados: {min_age}")
    print(f"Edad mayor de los empleados: {max_age}")

else:
    print("Error al obtener los datos de la API")
