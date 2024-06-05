# program.py

import hr
import StackImplent as s

salary_employee = hr.SalaryEmployee(1, "John Smith", 1500)
hourly_employee = hr.HourlyEmployee(2, "Jane Doe", 40, 15)
commission_employee = hr.CommissionEmployee(3, "Kevin Bacon", 1000, 250)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(
    [salary_employee, hourly_employee, commission_employee]
)


st = s.StackImplent()

print(st.push(11))
print(st.push(22))
print(st.isEmpty())
print(st.pop())
print(st.pop())
print(st.isEmpty())
print(st.push(23))
print(st.push(33))
print(st.push(44))
print(st.isFull())

for i in st.:
    print(i)