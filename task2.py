hours_worked=float(input("Enter the hours you worked:"))
hourly_rate=float(input("Enter the hourly rate you get:"))

#calculate gross_pay
gross_pay= hours_worked* hourly_rate


#calculate tax

if gross_pay <= 15600:
    tax = gross_pay * 10.5 / 100       # 10.5% tax for 0-15600
elif gross_pay <= 53500:
    tax = gross_pay * 17.5 / 100          # 17.5% tax for 15601-53500
elif gross_pay <= 78100:
    tax = gross_pay * 30 / 100       # 30% tax for 53501-78100
elif gross_pay <= 180000:
    tax = gross_pay * 33 / 100       # 33% tax for 78101-180000
else:
    tax = gross_pay * 39 / 100       # 39% tax for above 180000

# Calculate net pay
net_pay = gross_pay - tax

# Print results
print(f"Gross pay:{gross_pay}")
print(f"Tax:{tax}")
print(f"Net Pay:{net_pay}")

