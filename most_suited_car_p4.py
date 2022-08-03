# most suited car program
"""I will construct a program that will calculate which type of energy
efficient car is most suited for the user according to their requirements and
specifications"""

import emoji


# this function will ask the user for their name
def name():
    name_of_user = input("What is your name?")
    print("")
    print(emoji.emojize("Hello {} :grinning_face:".format(name_of_user)))
    print("")
    return name_of_user


# this function will inform the user about energy efficient cars
def information():
    while True:
        user_information = input(
            "Do you want background information about energy efficient cars?"
            ).lower()
        print("")
        if user_information == 'yes' or user_information == 'y':
            print(
                "Energy efficient cars are also known as clean cars and the"
                "government of New Zealand reduces the price of energy"
                "efficient cars using a clean car rebate of up to $8,625."
                "Energy efficient cars are cars that consume less or no petrol"
                "to reduce carbon emissions released by the vehicle. Reducing"
                "carbon emissions decreasing greenhouse gases that increase"
                "the temperature of Earth, causing climate change."
            )
            print("")
            break
        elif user_information == "no" or user_information == "n":
            break
        else:
            print("Please enter yes / y or no / n")
            print("")


# this function will calculate what type of energy efficient car is most suited
# for the user
def vehicle_type():
    vehicle_type_list = ["hybrid", "plug-in hybrid", "electric", "hydrogen"]
    vehicle_type = ""
    while True:
        try:
            user_kilometres = int(
                input("How many kilometres do you drive on average per week?"))
            print("")
            if user_kilometres <= 0:
                print("Please enter a positive number")
                print("")
            else:
                break
        except:
            print("Please enter a number")
            print("")

    while True:
        try:
            user_budget = int(
                input("What is your budget for the car you want to purchase?"))
            print("")
            if user_budget <= 0:
                print("Please enter a positive number")
                print("")
            else:
                break
        except:
            print("Please enter a number")
            print("")

    if user_kilometres >= 250 and user_budget <= 30000:
        vehicle_type = vehicle_type_list[0]

    elif user_kilometres >= 250 and user_budget > 30000:
        vehicle_type = vehicle_type_list[1]

    elif user_kilometres <= 250 and user_budget <= 30000:
        vehicle_type = vehicle_type_list[2]

    elif user_kilometres <= 250 and user_budget > 30000:
        vehicle_type = vehicle_type_list[3]

    print("The most suited type of energy efficient cars for you are {}"
          "vehicles".format(vehicle_type))
    print("")
    return vehicle_type


# this function informs the user about the energy efficient car the program has
# recommended for them
def car_information(car_type):
    if car_type == "hybrid":
        print(
            "Today's hybrid electric vehicles (HEVs) are powered by an"
            "internal combustion engine in combination with one or more"
            "electric motors that use energy stored in batteries. In a HEV,"
            "the extra power provided by the electric motor may allow for a"
            "smaller combustion engine. The vehicle uses regenerative braking"
            "and the internal combustion engine to charge. The vehicle"
            "captures energy normally lost during braking by using the"
            "electric motor as a generator and storing the captured energy in"
            "the battery."
        )
        print("")

    elif car_type == "plug-in hybrid":
        print(
            "Plug-in hybrid electric vehicles (PHEVs) are powered by an"
            "internal combustion engine in combination with one or more"
            "electric motors that use energy stored in batteries. In a PHEV,"
            "the extra power provided by the electric motor may allow for a"
            "smaller combustion engine. The vehicle uses regenerative braking"
            "and the internal combustion engine to charge internally. The"
            "vehicle captures energy normally lost during braking by using the"
            "electric motor as a generator and storing the captured energy in"
            "the battery. These batteries can be externally charged, similar"
            "to an electric car (BEVs) allowing more range than the average"
            "hybrid electric vehicle (HEVs)."
        )
        print("")

    elif car_type == "electric":
        print(
            "Electric cars (BEVs) are powered by energy from the battery."
            "These batteries can be externally charged. This energy is"
            "converted into power by an electric motor, which is used to drive"
            "the wheels."
        )
        print("")

    elif car_type == "hydrogen":
        print(
            "Hydrogen cars (FCEVs) are powered by hydrogen which enter the"
            "fuel cell from a tank and mix with oxygen to create water (H2O)"
            "in a chemical reaction, the water if released from the exhaust"
            "pipe which generates electricity that is used to power the motors"
            "that drive the wheels."
        )
        print("")


# this function will ask the user if they are looking for a 5-seater or a
# 7-seater
def car_seats():
    while True:
        seats = input(
            "Are you looking for a 5-seater or a 7-seater?")
        print("")
        if seats == "5":
            return '5'
        elif seats == "7":
            return '7'
        else:
            print("Please enter '5' or '7'")
            print("")
        print(seats, " is number of seats")


# this function will assign a key to the user according to the type of energy
# efficient car and number of seats
def ev_key(type, seatnumber):
    if type == "hybrid" and seatnumber == "5":
        return 'HEV 5'
    elif type == "hybrid" and seatnumber == "7":
        return 'HEV 7'
    elif type == "electric" and seatnumber == "5":
        return 'BEV 5'
    elif type == "electric" and seatnumber == "7":
        return 'BEV 7'
    elif type == "plug-in hybrid" and seatnumber == "5":
        return 'PHEV 5'
    elif type == "plug-in hybrid" and seatnumber == "7":
        return 'PHEV 7'
    elif type == "hydrogen" and seatnumber == "5":
        return 'FCEV 5'
    elif type == "hydrogen" and seatnumber == "7":
        return 'FCEV 7'
    else:
        return "no key"


# this function will ask the user if they are looking for a specific brand
def brand():
    valid_brands_list = ['toyota', 'nissan', 'hyundai', 'mitsubishi', 'tesla']
    while True:
        car_brand = input("Are you looking for a specific brand?").lower()
        print("")
        if car_brand == "y" or car_brand == "yes":
            wants_car_brand = True
            break
        elif car_brand == "n" or car_brand == "no":
            wants_car_brand = False
            return 'all_brand'
            break
        else:
            print("Please enter yes / y or no / n")

    if wants_car_brand is True:
        while True:
            print(valid_brands_list)
            brand_input = input("What brand are you looking for?").lower()
            if brand_input in valid_brands_list:
                print("You have selected {}".format(brand_input))
                print("")
                return brand_input
                break
            else:
                print("Please enter a valid brand")
                print("")


toyota_dict = {
    'HEV 5': ['Toyota Prius, Toyota Camry, Toyota Aqua, Toyota CH-R'],
    'HEV 7': ['Toyota Rav-4, Toyota Highlander'],
    'PHEV 5': ['Toyota Prius Prime'],
    'BEV 5': ['Toyota bz4x'],
    'FCEV 5': ['Toyota Mirai'],
    'BEV 7': ['Toyota has no 7 seater electric vehicles available in '
              'New Zealand']
}

nissan_dict = {
    'BEV 5': ['Nissan Leaf'],
    'BEV 7': ['Nissan has no 7 seater electric vehicles available in '
              'New Zealand'],
    'HEV 5': ['Nissan has no 5 seater hybrid vehicles available in '
              'New Zealand'],
    'HEV 7': ['Nissan has no 7 seater hybrid vehicles available in '
              'New Zealand'],
    'FCEV 5': ['Nissan has no 5 seater hydrogen vehicles available in '
               'New Zealand'],
    'FCEV 7': ['Nissan has no 7 seater hydrogen vehicles available in '
               'New Zealand']
}

hyundai_dict = {
    'BEV 5': ['Hyundai Ionic'],
    'BEV 7': ['Hyundai Kona'],
    'FCEV 7': ['Hyundai Nexo'],
    'HEV 5': ['Hyundai has no 5 seater hybrid vehicles available in '
              'New Zealand'],
    'HEV 7': ['Hyundai has no 7 seater hybrid vehicles available in '
              'New Zealand'],
    'FCEV 5': ['Hyundai has no 5 seater hydrogen vehicles available in '
               'New Zealand']
}

mitsubishi_dict = {
    'PHEV 7': ['Mitsubishi Outlander'],
    'BEV 5': ['Mitsubishi has no 5 seater electric vehicles available in '
              'New Zealand'],
    'BEV 7': ['Mitsubishi has no 7 seater electric vehicles available in '
              'New Zealand'],
    'HEV 5': ['Mitsubishi has no 5 seater hybrid vehicles available in '
              'New Zealand'],
    'HEV 7': ['Mitsubishi has no 7 seater hybrid vehicles available in '
              'New Zealand'],
    'FCEV 5': ['Mitsubishi has no 5 seater hydrogen vehicles available in '
               'New Zealand']
}

tesla_dict = {
    'BEV 5': ['Tesla Model 3'],
    'BEV 7': ['Tesla has no 7 seater electric vehicles available in '
              'New Zealand'],
    'HEV 5': ['Tesla has no 5 seater hybrid vehicles available in '
              'New Zealand'],
    'HEV 7': ['Tesla has no 7 seater hybrid vehicles available in '
              'New Zealand'],
    'FCEV 5': ['Tesla has no 5 seater hydrogen vehicles available in '
               'New Zealand'],
    'FCEV 7': ['Tesla has no 7 seater hydrogen vehicles available in '
               'New Zealand']
}

all_brand_dict = {
    'HEV 5': ['Toyota Prius, Toyota Camry, Toyota Aqua, Toyota CH-R'],
    'HEV 7': ['Toyota Rav-4, Toyota Highlander'], 'PHEV 5':
             ['Toyota Prius Prime'],
    'PHEV 7': ['Mitsubishi Outlander'],
    'BEV 5': ['Toyota bz4x', 'Nissan Leaf', 'Hyundai Ionic', 'Tesla Model 3'],
    'BEV 7': ['Hyundai Kona'],
    'FCEV 5': ['Toyota Mirai'],
    'FCEV 7': ['Hyundai Nexo']
}


def ev_model(car_brand, car_key):
    if car_brand == 'toyota':
        return toyota_dict[car_key]
    elif car_brand == 'nissan':
        return nissan_dict[car_key]
    elif car_brand == 'hyundai':
        return hyundai_dict[car_key]
    elif car_brand == 'mitsubishi':
        return mitsubishi_dict[car_key]
    elif car_brand == 'tesla':
        return tesla_dict[car_key]
    elif car_brand == 'all_brand':
        return all_brand_dict[car_key]
    else:
        return ["No models available"]


user_name = name()
information()
user_vehicle_type = vehicle_type()
car_information(user_vehicle_type)
user_car_seats = car_seats()
user_car_key = ev_key(user_vehicle_type, user_car_seats)
user_car_brand = brand()
user_ev_model = ev_model(user_car_brand, user_car_key)

print("From the data you gave, the most suited ev car models for you are:")
for x in user_ev_model:
    print(x)

