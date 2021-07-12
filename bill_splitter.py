from decimal import *

def main():
    total_bill = Decimal(input('How much is the bill? '))
    total_tax = int(input('How much is the tax (%)? '))
    total_tip = int(input('How much is the tip (%)? '))
    total_person = int(input('How many people are paying? '))

    total_after_tax = ((Decimal(total_tax/100) +1) * total_bill)
    total_after_tip = ((Decimal(total_tip/100) +1) * total_after_tax)
    payment = total_after_tip / total_person
    print(f'Bill before tax: {total_bill}')
    print(f'Bill after tax: {total_after_tax}')
    print(f'Bill after tip: {total_after_tip}')
    print(f'Bill per person: {payment}')


main()
