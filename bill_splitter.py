from decimal import *

def main():
    totalBill = input('How much is the bill? ')
    b = Decimal(totalBill)
    print(b)
    tax = input('How much is tax (%)? ')
    print(tax.count(tax))
    taxPercent = Decimal(percentConvert(tax))
    print(b*taxPercent)



def percentConvert(t):
    st = str(t)
    if st.count(st)==1:
        t2 = f'1.0{st}'
        return t2
    elif st.count(st)==2:
        t3 = f'1.{st}'
        return t3
    else:
        tE = st
        return tE


main()
