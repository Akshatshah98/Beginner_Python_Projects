from random import randint

print("Welcome to Rolling Dice")
usr_input = "R"
while usr_input == "R":
    value = randint(1,6)
    if value == 1:
        print("===========")
        print("||       ||")
        print("||   0   ||")
        print("||       ||")
        print("===========")
        

    if value == 2:
        print("===========")
        print("||   0   ||")
        print("||       ||")
        print("||   0   ||")
        print("===========")
        

    if value == 3:
        print("===========")
        print("|| 0     ||")
        print("||   0   ||")
        print("||     0 ||")
        print("===========")
        

    if value == 4:
        print("===========")
        print("|| 0   0 ||")
        print("||       ||")
        print("|| 0   0 ||")
        print("===========")
        


    if value == 5:
        print("===========")
        print("|| 0   0 ||")
        print("||   0   ||")
        print("|| 0   0 ||")
        print("===========")
        


    if value == 6:
        print("===========")
        print("|| 0   0 ||")
        print("|| 0   0 ||")
        print("|| 0   0 ||")
        print("===========")
                                           
    roll_input = input("Type 'R'and press enter to Roll the Dice and Press 'X' to exit:  ")
    usr_input = roll_input.upper()

input_exit = usr_input.upper()
if input_exit == "X":
    print("Thanks for using the Simulator :) ")
    quit()
