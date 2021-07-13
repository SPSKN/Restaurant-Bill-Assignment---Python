from decimal import *
from math import *
def main():
    total_bill = Decimal(input('How much is the bill? '))
    total_tax = int(input('How much is the tax (%)? '))
    total_tip = int(input('How much is the tip (%)? '))
    total_person = int(input('How many people are paying? '))

    total_after_tax = ((Decimal(total_tax/100) +1) * total_bill)
    total_after_tip = ((Decimal(total_tip/100) +1) * total_after_tax)
    payment = total_after_tip / total_person
    print(f'Bill before tax: {round(total_bill,2)}')
    print(f'Bill after tax: {round(total_after_tax,2)}')
    print(f'Bill after tip: {round(total_after_tip,2)}')
    print(f'Bill per person: {round(payment,2)}')


main()
