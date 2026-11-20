"""Task 3 (Translated): Equivalent Pandas DataFrame query."""
import pandas as pd

employees = pd.DataFrame([
    {"name": "Adagiri Ansika", "salary": 85000},
    {"name": "Rohan", "salary": 45000},
    {"name": "Meera", "salary": 62000},
])

result = employees.loc[employees["salary"] > 50000, ["name", "salary"]]
print(result.to_string(index=False))
