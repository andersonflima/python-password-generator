import random

def verify_conversion(input, type, default):
    try:
        input = type(input)
        return input
    except:
        return default


def main():
    upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    lower_letters = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'.lower()
    digits = '0123456789'
    symbols = '!@#$%&*()'

    upper, lower, digit, symbol = False,False,False,False

    passwd = ''

    if(verify_conversion(input('Do you want uppercase letters S/n: ').lower(), str,'s') == 's' ):
        upper = True

    if(verify_conversion(input('Do you want lowercase letters S/n: ').lower(),str,'s' ) == 's' ):
        lower = True

    if(verify_conversion(input('Do you want digits S/n: ').lower(),str,'s' ) == 's' ):
        digit = True

    if(verify_conversion(input('Do you want symbols S/n: ').lower(),str,'s' ) == 's' ):
        symbol = True

    lenght = verify_conversion(input('choose your password lenght: ') ,int,20)
    amount = verify_conversion(input('choose how many passwords to show: ') ,int,10)

    if upper:
        passwd += upper_letters
    if lower:
        passwd += lower_letters
    if digit:
        passwd += digits
    if symbol:
        passwd += symbols

    try:
        for x in range(amount):
            password = ''.join(random.sample(passwd, lenght))
            print(password)
    except:
        print('the password possibilities are too short for the chosen length ')

if __name__=='__main__':
    main()