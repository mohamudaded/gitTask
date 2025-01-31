name = input("Enter your name:")
color = input("Enter your favorite color:")

# Added a conditional block

if name == "Aded" and color == "blue":
    print(f"Welcome {name}, access granted!")
    
    num1 = 5
    num2 = 7
    
    if num1 > num2:
        num1 * num2
    else:
        num2 - num1
else:
    print("Error, wrong name entered and color. Please try again")
