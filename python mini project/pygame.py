import random
user=0
computer=0


options=["rock","paper","siccor"]

while True:
    user_type= input("type rock/paper/siccor or exit").lower()
    if user_type== "exit":
       quit()
    if user_type not in options :
        continue
    random_num=rrandom_number=random.randint(0,2)

    computer_type = options[random_num]

    print("computer", computer_type)

    if user_type == "rock" and computer_type =="siccor": 
       print("You won") 
       user +=1

    elif user_type == "paper" and computer_type =="rock":
       print("You won")
       user +=1

    elif user_type == "siccor" and computer_type =="rock":
        print("You won")
        user +=1

    else:
       print("you lost")
       computer+=1

    print("you won",user)
    print("computer",computer)

