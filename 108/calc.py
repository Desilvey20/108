#Cal.py
#Extreme Calculator
#David
def menu():
    print("="*30)
    print("Extreme Calc")
    print("by David")
    print("="*30)
    print("[1] Sum")
    print("[2] Subtract")
    print("[3] Mult")
    print("[4] Div")
    print("[q] Exit")

option = ''
while option!="q":
    menu()
    option = input('Please, select an option: ')
    #print('the selected option is ' + option)

    #ask for the number 1
    num1 = float(input('enter the first number: '))

    #ask for the number 2
    num2 = float(input('enter the second number: '))

    print(f"DEBUG: num1: {num1} num2: {num2}")

    result = 0
    if option=="1":
        result = num1+num2
        print(f"The result is: {result}")

    elif option=="2":
        result = num1-num2
        print(f"The result is: {result}")
    elif option=="3":
        result = num1*num2
        print(f"The result is: {result}")
    elif option=="4":
        if num2 != 0:
            result = num1/num2
            print(f"The result is: {result}")
        else:
            print("We can not divide by zero!!")
    input('Press enter to continue...')
