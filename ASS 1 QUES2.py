# question 2

# User input for gross income and number of dependents
gross_income = float(input("Enter your gross income: "))
num_dependents = int(input("Enter the number of dependents: "))

# Constants for tax laws
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000
DEPENDENT_DEDUCTION = 3000

# Calculation of taxable income and income tax
taxable_income = gross_income - STANDARD_DEDUCTION - (DEPENDENT_DEDUCTION * num_dependents)
income_tax = taxable_income * TAX_RATE

# Output of income tax
print("Your income tax is: $" + str(round(income_tax, 2)))
