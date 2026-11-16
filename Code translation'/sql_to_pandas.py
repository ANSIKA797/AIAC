import pandas as pd

# Create sample employee data
data = {
    "name": ["Anu", "Rahul", "Priya", "Kiran", "Arjun"],
    "salary": [45000, 60000, 75000, 40000, 55000]
}

# Create a DataFrame
employees = pd.DataFrame(data)

# Apply the equivalent SQL condition
result = employees.loc[
    employees["salary"] > 50000,
    ["name", "salary"]
]

print("Employees with salary greater than 50000:")
print(result.to_string(index=False))