"""
Practical 01 — Self Study Assignment
Problem: Statistical analysis on employee data — Average, Max, Min, Sum
"""

def analyze_employee_data(salaries):
    """Perform statistical analysis on employee salary data"""
    if not salaries:
        print("No data to analyze")
        return
    
    average = sum(salaries) / len(salaries)
    max_salary = max(salaries)
    min_salary = min(salaries)
    total_salary = sum(salaries)
    
    return {
        'average': average,
        'max': max_salary,
        'min': min_salary,
        'sum': total_salary,
        'count': len(salaries)
    }

# Sample employee data (salaries in ₹)
employee_salaries = []

print("Enter employee salary data (type 'done' when finished):")
while True:
    try:
        salary_input = input("Enter salary (₹): ")
        if salary_input.lower() == 'done':
            break
        salary = float(salary_input)
        if salary >= 0:
            employee_salaries.append(salary)
        else:
            print("Salary cannot be negative. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Analyze data
if employee_salaries:
    stats = analyze_employee_data(employee_salaries)
    
    print(f"\n--- Statistical Analysis ---")
    print(f"Total Employees: {stats['count']}")
    print(f"Total Salary: ₹{stats['sum']:,.2f}")
    print(f"Average Salary: ₹{stats['average']:,.2f}")
    print(f"Maximum Salary: ₹{stats['max']:,.2f}")
    print(f"Minimum Salary: ₹{stats['min']:,.2f}")
else:
    print("No salary data entered.")
