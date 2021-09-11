print("MAIN MENU\n1.– List the best musical group ever\n2.– List the best sports team ever\n3.– Quit")

while True:
    number = input('Enter the number for your choice:')
    if number == '1' :
        print('The Beatles are the best ever')

    elif number == '2' :
        print('The Cubs are the best ever')

    elif number == '3' :
        print('OK!  Hope you learned something.')
        break
    else :
        print('That’s not one of the choices. Try again.')
        print("MAIN MENU\n1.– List the best musical group ever\n2.– List the best sports team ever\n3.– Quit")
