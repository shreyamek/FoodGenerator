import random

var = 0
while var ==0:

    random_variable = 1

    while random_variable == 1:
        print("Hi. Our service will help you pick a food item to eat by randomly picking a food item. What type of food do you want to eat today?")
        print("1. Unhealthy")
        print("2. Healthy")
        option1 = int(input("Enter the number: "))
        if option1 == 1 or option1 == 2:
            break
        else:
            print("Please enter a valid number")


    while option1 == 1:
        print("  ")
        print("Your food category was unhealthy.")
        print("Which meal do you want to choose from?")
        print("1. Breakfast")
        print("2. Lunch")
        print("3. Dinner")
        print("4. Snack")

        unhealthy = int(input("Enter the number: "))
        print("  ")
        if unhealthy == 1 or unhealthy ==2 or unhealthy == 3 or unhealthy ==4:
            if unhealthy == 1:
                unhealthy_bmenu = ["pancakes", "cake", "french toast", "waffles", "banana bread", "cereal"]
                print(random.choice(unhealthy_bmenu))
                break

            elif unhealthy == 2:
                unhealthy_lmenu = ["chicken fried rice", "pizza", "french fries", "mac and cheese", "pasta", "chicken sandwich"]
                print(random.choice(unhealthy_lmenu))
                break

            elif unhealthy == 3:
                unhealthy_dmenu = ["chicken fried rice", "pizza", "mac and cheese", "pasta", "chicken sandwich"]
                print(random.choice(unhealthy_dmenu))
                break

            elif unhealthy == 4:
                unhealthy_smenu = ["potato chips", "nachos with cheese or salsa", "chocolate bars", "candy", "cookies"]
                print(random.choice(unhealthy_smenu))
                break
            else:
                print("Please enter a valid number")



    while option1 == 2:
        print("  ")
        print("Your food category was healthy.")
        print("Which meal do you want to choose from?")
        print("1. Breakfast")
        print("2. Lunch")
        print("3. Dinner")
        print("4. Snack")

        healthy = int(input("Enter the number: "))
        print("  ")
        if healthy == 1 or healthy ==2 or healthy == 3 or healthy ==4:
            if healthy == 1:
                healthy_bmenu = ["baked oats", "stovetop oats", "rice cakes with toppings", "smoothies", "scrambled eggs", "avocado toast"]
                print(random.choice(healthy_bmenu))
                break

            elif healthy == 2:
                healthy_lmenu = ["avocado and egg sandwich", "quinoa pear salad", "chicken burrito bowl with rice and peans", "protein salad", "vegetable soup"]
                print(random.choice(healthy_lmenu))
                break

            elif healthy == 3:
                healthy_dmenu = ["avocado and egg sandwich", "quinoa pear salad", "chicken burrito bowl with rice and beans", "protein salad", "vegetable soup"]
                print(random.choice(healthy_dmenu))
                break

            elif healthy == 4:
                healthy_smenu = ["rice cakes", "greek yogurt with fruits", "mixed nuts", "apple slices with peanut butter", "healthy smoothie"]
                print(random.choice(healthy_smenu))
                break
            else:
                print("please enter a valid number")
        else:
            print("please enter a valid number")

    print("  ")
    print("Would you like to restart?")
    print("1. Yes")
    print ("2. No")
    print("  ")
    restart = int(input("Enter the number: "))
    if restart == 1:
        var == 0
    else:
        var == 1
        print("Thanks for using our service!")
        break

