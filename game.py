cave = 'starting'
donut = 0
game_running = True
while game_running:
    if cave == 'starting' :
        print("You are Lost In a Jungle, You have found a cave to live inside but you have nothing to eat!. You decide to explore the cave since its too big , Now you have two paths infront of you, an wooden door and a ravine")
        print("If You want to open the door type 1 and if you want to pass from the ravin type 2")

        answer = input("1-2: ")

        if answer == "1":
            cave = "door"
        elif answer == "2":
                cave = "ravin"
        else:
            print("Are You Stupid, You only Have Two Options 1 and 2")
    elif cave == "door":
        if donut >= 2:
            print("You Win!") 
            game_running = False
        else:
            print("You dont have enough energy to open the door, You are Starving to Death")
            print("You Died Because Of Hunger, Try choosing Another Way!")
            cave = 'starting'
    elif cave == "ravin":
        print("You Have Entered the ravin, its too dangerous. On your left side you see a bear and its approaching towards you, you need to make a decision fast")
        print("Press 1 if you want to act dead and press 2 if you want to fight with bear")

        answer = input("1-2 :")
        if answer == "1":
            print("The Bear Was Stupid, It left you thinking a dead body. Congratulations, YOU ARE SAFE!!")
            print("You Are Lucky, Rescue Team Found You Before You Starve To Death")
            game_running = False
            break
        elif answer == "2":
            print("You are not too strong to fight with a bear, you were already starving to death")
            print("The Bear Had A Good Lunch, YOU DIED!!")






