# mortgage.py
#
# Exercise 1.7
principal = 500_000.0
rate = 0.05
payment = 2_684.11
total_paid = 0.0

months = 0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1_000


while principal > 0:
    months += 1
    if principal < payment:
        payment -= principal
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if extra_payment_start_month <= months <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment

    if principal > 0:
        print(f'Month: {months:3d} - Paid:{total_paid:10.2f} - Unpaid:{principal:10.2f}')
    else:
        print(f'Month: {months:3d} - Paid:{total_paid:10.2f} - Unpaid:{(principal == 0):10.2f}\n')

print(f'Total months: \t{months}')
print(f'Total paid: \t{total_paid:.2f}')
