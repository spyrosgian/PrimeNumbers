#---------------------------------------------------------------------------------------
#PrimeNumbers
#---------------------------------------------------------------------------------------

#Input number (number should be integer).
Number = input ('Please enter a decimal number: ')

while True:

    #If statement to check if input is integer.
    if Number.isalpha() == False:
        if (float (Number)/(int (float(Number)))) != 1:
            print ('Number is not prime number.')
            break

    #If statement to check if input has more than 3 characters.
    if float (len (Number)) > 3:
        print ('More than 3 characters.')
        break

    #If statement to check if input contains characters a-z.
    if Number.isalpha() == True:
        print ('Invalid input.')
        break

    Number = int (Number)

    #If/else statement to check if input is prime number.
    if Number > 1:
        for i in range(2, Number):
            if (Number % i) == 0:
                print ('Number entered is not a prime number.')
                break
            else:
                print ('Number entered is a prime number.')
                break
    else:
        print ('Number entered is not a prime number.')
        break
    break


