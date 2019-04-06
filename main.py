import random

user_choice = input("Elige piedra, papel o tijera: ")
user_choice = user_choice.lower()
machine_random = random.randint(1,3)
machine_choice = "a"

if(machine_random == 1):
    machine_choice = "piedra"
elif(machine_random == 2):
    machine_choice = "papel"
elif(machine_random == 3):
    machine_choice = "tijera"

if(machine_choice == user_choice):
    print("Vosotros habéis sacado " + machine_choice + ", por lo que es empate.")
elif(machine_choice == "piedra" and user_choice == "papel" or
     machine_choice == "papel" and user_choice == "tijera" or
     machine_choice == "tijera" and user_choice == "piedra"):
    print("El pc ha sacado " + machine_choice + " y usted ha sacado " + user_choice + ", por lo que has ganado!!!")
elif(user_choice == "piedra" or user_choice == "papel" or user_choice == "tijera"):
    print("El pc ha sacado " + machine_choice + " y usted ha sacado " + user_choice + ", por lo que has perdido")
else:
     print("Has introducido mal los datos")
