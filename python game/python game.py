import random
pick = ["rock","paper","scissor"]
your_score = 0
computer_score = 0
print("welcome to the game")
end = 1
while(end):
    human_input=input("enter your choice ! \"rock\" \"paper\" \"scissor\" \n")
    computer_input = random.choice(pick)
    print(computer_input)
    if human_input == computer_input:
        print("Tie !")
    elif human_input == "rock":
        if computer_input == "paper":
            print("you lose")
            computer_score = computer_score+1
        else:
                your_score = your_score+1
                print("you won")
    elif human_input == "paper":
        if computer_input == "rock":
                your_score = your_score+1
                print("you won")
        else:
            computer_score = computer_score+1
            print("you lose")
    elif human_input == "scissor":
        if computer_input == "rock":
             computer_score = computer_score+1
             print("you lose")
        else:
            your_score = your_score+1
            print("you won")
    else:
        print("Type correct choice ")
    print("\n")
    end = int(input("Wanna Quit ? Press 0 to exit or 1 to continue! "))
print("##############")
print("Your score is ",your_score)
print("Computer score is ",computer_score)
print("##############")
    
        
