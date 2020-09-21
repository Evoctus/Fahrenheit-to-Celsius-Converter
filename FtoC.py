CheckInput = 1
while CheckInput == 1:
    while True:
        Fahrenheit = (input("Enter a temperature in Fahrenheit:"))
        if Fahrenheit.isdigit():
            Fahrenheit = int(Fahrenheit)
            break
        else:
            print ("Please type out an integer.")      
    Celsius = (Fahrenheit - 32) * 5.0/9.0
    print (Celsius)
    while True:
        UserInput = input("Calculate again? Yes or No?")
        if UserInput.upper() == "YES":
            break
        elif UserInput.upper() == "NO":
            CheckInput = 2
            break
        else:
            print ("Please enter Yes or No")
            
            
         
        
