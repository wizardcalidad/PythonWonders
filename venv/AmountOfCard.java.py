def charge_amt():
    amt = int(input('How much do you wan to charge: '))
    if amt == 5 or amt == 10:
        return amt
    elif amt == 25:
        return  amt + 3
    elif amt == 50:
        return amt + 8
    elif amt == 100:
        return  amt + 20
    else:
        print('Invalid Amount')
print(charge_amt())