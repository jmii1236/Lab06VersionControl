def encoder(passw):
    newpass = ""
    for i in range (0, len(passw)):
        intpassw = int(passw[i])
        intpassw += 3
        newpass += str(intpassw)
        i += 1
    return "Your password has been encoded and stored!"
pass
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
            password = str(input("Please enter your password to encode: "))
        if option == 1:
            print(encoder(password))
        if option == 2:
            pass
        if option == 3:
            break

