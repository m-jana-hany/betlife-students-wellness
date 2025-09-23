import time 

def pr_pause(message):
    print(message)
    time.sleep(2)

name = input("please enter your name:")
time.sleep(2)
Gender = input("please enter your Gender:")
time.sleep(2)
Email = input("please enter your Email:")
time.sleep(2)
Phone_Number = input("please enter your Phone Number:")
time.sleep(2)
Number_of_Classes = input("please enter your Number of Classes:")
time.sleep(2)
pr_pause("Your Details:")
pr_pause(name)
pr_pause(Gender)
pr_pause(Email)
pr_pause(Phone_Number)
pr_pause(Number_of_Classes)


