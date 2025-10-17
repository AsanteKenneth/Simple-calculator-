
power=input("enter 'on' to start or 'off' to stop:")
while power !='off':
    first_number=float(input("enter the first number: "))
    operator=input("enter the operational sign(+,-,*,/)")
    second_number=float(input("enter the second number: "))
    if operator=='+':
        add=first_number + second_number
        print(f"the answer is {add}")
    elif operator=='-':
        subtract=first_number - second_number
        print(f"the answer is {subtract}")    
    elif operator=='*':
        times=first_number * second_number
        print(f"the answer is {times}")   
    elif operator=='/':
        divide=first_number / second_number
        print(f"the answer is {divide}")
    else:
        print("check the operator you entered well")
        print('type stop to stop calculating')
