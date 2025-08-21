#importing necessary libraries
import pandas as pd
import numpy as np

#loading the data from the csv file
employee_df = pd.read_csv('employee_data.csv')

#setting EmployeeID as Index
employee_df.set_index('EmployeeID', inplace=True)

#displaying the information of the dataframe
print("Initial information about the dataframe:\n")
employee_df.info()
print("\n------\n")

#highest paid engineer
engineering_department = employee_df['Department'] == 'Engineering'
print(f"\nThe employee in Engineering department with the highest salary:\n\n{employee_df[engineering_department].sort_values('Salary', ascending=False).head(1)}\n")
print("\n------\n")

#new employee bonus column
employee_df['StartDate'] = pd.to_datetime(employee_df['StartDate'])
employee_df['Bonus'] = np.where(employee_df['StartDate']>='2023-01-01', 2000, 0)
print(f"DataFrame after addition of the new Bonus feature:\n\n{employee_df[['FirstName', 'LastName', 'StartDate', 'Bonus']]}\n")
print("\n------\n")

#departmental salary report
groupby_department = employee_df.groupby('Department')
print(f"Department wise report on Average Salaries (Highest to Lowest)\n\n{groupby_department['Salary'].mean().sort_values(ascending=False)}\n")
print("\n------\n")

#lowest salary employee from sales
sales_employee_df = employee_df[employee_df['Department'] == 'Sales']
print(f"Lowest salary employee from sales department:\n\n{sales_employee_df.sort_values(by='Salary').head(1)}")
print("\n------\n")
