# most suited car program
"""I will construct a program that will calculate which type of energy efficient car is most suited for the user
    according to their requirements and specifications"""

import emoji


# this function will ask the user for their name
def name():
    user_name = input("What is your name?")
    print(emoji.emojize("Hello {} :smiling_face:".format(user_name)))


# this function will get the amount of kilometres the user drives on average
def kilometres():
    user_kilometres = int(input("How many kilometres do you drive on average per week?"))
    return user_kilometres


# this function will get the amount of money the user spends on petrol on average
def petrol():
    user_petrol = int(input("How much do you spend on petrol on average per week?"))
    return user_petrol


# this function will get the budget of the user for the car they want to purchase
def budget():
    user_budget = int(input("What is your budget for the car you want to purchase?"))
    return user_budget


# this function will decide calculate what type of energy efficient car is most suited for the user
def ev_vehicle(user_kilometres, user_budget, user_petrol):
    ev_vehicle_list = ["hybrid", "plug-in hybrid", "electric", "hydrogen"]
    user_ev_vehicle = ""

    if user_kilometres >= 250 and 0 <= user_budget <= 30000:
        user_ev_vehicle = ev_vehicle_list[0]

    elif user_kilometres >= 250 and 0 <= user_budget >= 30000:
        user_ev_vehicle = ev_vehicle_list[1]

    elif user_kilometres <= 250 and 30000 <= user_budget <= 60000:
        user_ev_vehicle = ev_vehicle_list[2]

    elif user_kilometres <= 250 and 30000 <= user_budget >= 60000:
        user_ev_vehicle = ev_vehicle_list[3]

    else:
        pass

    print(user_ev_vehicle)


name()

