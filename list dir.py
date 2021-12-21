import os
from playsound import playsound
print("Hello")
print(os.listdir())
# list dir with sound 
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        #num1 = float(input("Enter first number: "))
        # num2 = float(input("Enter first number: "))
        if choice == '1':
            playsound('C:\\Users\\spark\\Downloads\\chillabstract12099.mp3')

        elif choice == '2':
            playsound('C:\\Users\\spark\\Downloads\\techno.mp3')

# check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break

else:
        print("Invalid Input")