import sys
loop = True
while loop:
    CheckInput = (input("Fahrenheit into Celsius or Celsius into Fahrenheit?"))
    if CheckInput.upper() == "FAHRENHEIT INTO CELSIUS":
        CheckInput = 1
    elif CheckInput.upper() == "CELSIUS INTO FAHRENHEIT":
        CheckInput = 2
    else:
        print ("Please enter Fahrenheit into Celsius or Celsius into Fahrenheit")
        loop = True
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
        print ("Degrees Celsius")
        RepeatInput = 1
        while RepeatInput == 1:
            UserInput = input("Calculate again? Yes or No?")
            if UserInput.upper() == "YES":
                break
            elif UserInput.upper() == "NO":
                sys.exit()
            else:
                print ("Please enter Yes or No")
    while CheckInput == 2:
        while True:
            Celsius = (input("Enter a temperature in Celsius:"))
            if Celsius.isdigit():
                Celsius = int(Celsius)
                break
            else:
                print ("Please type out an integer.")
        Fahrenheit = (Celsius * 9.0/5.0) + 32
        print (Fahrenheit)
        print ("Degrees Fahrenheit")
        while True:
            UserInput = input("Calculate again? Yes or No?")
            if UserInput.upper() == "YES":
                    break
            elif UserInput.upper() == "NO":
                sys.exit()
            else:
                print ("Please enter Yes or No")
                
            
         
        

