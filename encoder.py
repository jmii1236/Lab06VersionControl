def encoder(passw):
    newpass = ""
    for i in range (0, len(passw)):
        intpassw = int(passw[i])
        intpassw += 3
        newpass += str(intpassw)
        i += 1
    print("Your password has been encoded and stored!")
    return newpass

def decoder(passw):
    newpass = ''
    for digit in passw:
        digit = int(digit)
        newpass = newpass + str(digit-3)
    return newpass

if __name__ == '__main__':
    while True:
        option = 1
        if 0 < option < 4:
            print("\nMenu"
                  "\n------------"
                  "\n1. Encode"
                  "\n2. Decode"
                  "\n3. Quit")
            option = int(input("\nPlease enter an option: "))
        if option == 1:
            password = str(input("Please enter your password to encode: "))
            password = encoder(password)
        if option == 2:
            print(f'The encoded password is {password}, the original password is {decoder(password)}')
        if option == 3:
            break

