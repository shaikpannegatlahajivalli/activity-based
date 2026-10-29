# Employee Payroll and Deduction Analysis: 
#Calculate gross salary from basic pay, allowances, overtime, and incentives; apply progressive deductions and generate a formatted salary statement.
basic=int(input("enter a number:"))
allowances=int(input("enter a number:"))
overtime=int(input("enter a number:"))
incentives=int(input("enter anumber:"))
gross=basic+allowances+overtime+incentives
if gross<=20000:
    deduction=gross*0.05
elif gross<=30000:
    deduction=gross*0.10
else:
    deduction=gross*0.15
net=gross-deduction
print("Basic=",basic)
print("Allowances=",allowances)
print("Overtime=",overtime)
print("Incentives=",incentives)
print("Deduction=",deduction)
print("Gross=",gross)
