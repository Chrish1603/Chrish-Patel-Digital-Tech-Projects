# most suited car program
"""I will construct a program that will calculate which type of energy efficient car is most suited for the user
    according to their requirements and specifications"""

import emoji


# this function will ask the user for their name
def name():
    user_name = input("What is your name?")
    print("")
    print(emoji.emojize("Hello {} :grinning_face:".format(user_name)))
    print("")


# this function will inform the user about energy efficient cars
def information():
    user_information = input("Do you want background information about energy efficient cars?").lower()
    print("")

    if user_information == 'yes' or user_information == 'y':
        print(
            "Energy efficient cars are also known as clean cars and the government of New Zealand reduces the price of "
            "energy efficient cars using a clean car rebate of up to $8,625. Energy efficient cars are cars that "
            "consume less or no petrol to reduce carbon emissions released by the vehicle. Reducing carbon emissions "
            "decreasing greenhouse gases that increase the temperature of Earth, causing climate change. "
        )
        print("")

    elif user_information == "no" or user_information == "n":
        pass

    else:
        print("Please enter yes / y or no / n")
        print("")


# this function will calculate what type of energy efficient car is most suited for the user
def ev_vehicle():
    ev_vehicle_list = ["hybrid", "plug-in hybrid", "electric", "hydrogen"]
    user_ev_vehicle = ""

    user_kilometres = int(input("How many kilometres do you drive on average per week?"))
    print("")

    user_petrol = int(input("How much do you spend on petrol on average per week?"))
    print("")

    user_budget = int(input("What is your budget for the car you want to purchase?"))
    print("")

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

    print("The most suited type of energy efficient cars for you are {} vehicles".format(user_ev_vehicle))
    print("")


# this function informs the user about the energy efficient car the program has recommended for them
def car_information(user_ev_vehicle):
    if user_ev_vehicle == "hybrid":
        print(
            "Today's hybrid electric vehicles (HEVs) are powered by an internal combustion engine in "
            "combination with one or more electric motors that use energy stored in batteries. "
            "In a HEV, the extra power provided by the electric motor may allow for a smaller "
            "combustion engine. The vehicle uses regenerative braking and the internal combustion engine "
            "to charge. The vehicle captures energy normally lost during braking by using the electric "
            "motor as a generator and storing the captured energy in the battery."
        )
        print("")

    elif user_ev_vehicle == "plug-in hybrid":
        print(
            "Plug-in hybrid electric vehicles (PHEVs) are powered by an internal combustion engine in"
            "combination with one or more electric motors that use energy stored in batteries. In a PHEV, the "
            "extra power provided by the electric motor may allow for a smaller combustion engine. The vehicle uses "
            "regenerative braking and the internal combustion engine to charge internally. The vehicle captures "
            "energy normally lost during braking by using the electric motor as a generator and storing the captured "
            "energy in the battery. These batteries can be externally charged, similar to an electric car (BEVs)"
            "allowing more range than the average hybrid electric vehicle (HEVs)."
        )
        print("")

    elif user_ev_vehicle == "electric":
        print(
            "Electric cars (BEVs) are powered by energy from the battery. These batteries can be externally charged. "
            "This energy is converted into power by an electric motor, which is used to drive the wheels."
        )
        print("")

    elif user_ev_vehicle == "hydrogen":
        print(
            "Hydrogen cars (FCEVs) are powered by hydrogen which enter the fuel cell from a tank and mix with oxygen "
            "to create water (H2O) in a chemical reaction, the water if released from the exhaust pipe which generates "
            "electricity that is used to power the motors that drive the wheels."
        )
        print("")

    else:
        pass


# this function will ask the user if they are looking for a 5-seater or a 7-seater
def car_seats():
    user_seat_number = int(input("Are you looking for a 5-seater or a 7-seater?"))
    print("")
    if user_seat_number == "5":
        pass
    elif user_seat_number == "7":
        pass
    else:
        print("Please enter '5' or '7'")
        print("")

    return user_seat_number


# this function will assign a key to the user according to the type of energy efficient car and number of seats
def ev_key(user_ev_vehicle, user_seat_number):
    user_key = ""

    if user_ev_vehicle == "hybrid" and user_seat_number == "5":
        user_key = 'HEV 5'

    elif user_ev_vehicle == "hybrid" and user_seat_number == "7":
        user_key = 'HEV 7'

    elif user_ev_vehicle == "electric" and user_seat_number == "5":
        user_key = 'BEV 5'

    elif user_ev_vehicle == "electric" and user_seat_number == "7":
        user_key = 'BEV 7'

    elif user_ev_vehicle == "plug-in hybrid" and user_seat_number == "5":
        user_key = 'PHEV 5'

    elif user_ev_vehicle == "plug-in hybrid" and user_seat_number == "7":
        user_key = 'PHEV 7'

    elif user_ev_vehicle == "hydrogen" and user_seat_number == "5":
        user_key = 'FCEV 5'

    elif user_ev_vehicle == "hydrogen" and user_seat_number == "7":
        user_key = 'FCEV 7'

    else:
        pass


# this function will ask the user if they are looking for a specific brand
def brand():
    valid_brands_list = ['toyota', 'nissan', 'hyundai', 'mitsubishi', 'tesla']
    car_brand = input("Are you looking for a specific brand?").lower()
    print("")
    user_brand = ""

    if car_brand == "yes" or car_brand == "y":
        user_brand_input = input("What brand are you looking for?").lower()
        print("")

        # this for loop checks if the brand the user input is in valid_brands_list
        for x in valid_brands_list:
            if user_brand_input in x:
                user_brand = user_brand_input
                print("You have selected {}".format(user_brand))
                print("")
            else:
                pass

    elif car_brand == "no" or car_brand == "n":
        user_brand = 'all_brand'

    else:
        print("Please enter yes / y or no / n")
        print("")


# this function will have a list of cars from brands
def brands_dict():
    toyota_dict = {'HEV 5': 'Toyota Prius, Toyota Camry, Toyota Aqua, Toyota CH-R',
                   'HEV 7': 'Toyota Rav-4, Toyota Highlander',
                   'PHEV 5': 'Toyota Prius Prime',
                   'BEV 5': 'Toyota bz4x',
                   'FCEV 5': 'Toyota Mirai',
                   'BEV 7': 'Toyota has no 7 seater electric vehicles available in New Zealand'
                   }

    nissan_dict = {'BEV 5': 'Nissan Leaf',
                   'BEV 7': 'Nissan has no 7 seater electric vehicles available in New Zealand',
                   'HEV 5': 'Nissan has no 5 seater hybrid vehicles available in New Zealand',
                   'HEV 7': 'Nissan has no 7 seater hybrid vehicles available in New Zealand',
                   'FCEV 5': 'Nissan has no 5 seater hydrogen vehicles available in New Zealand',
                   'FCEV 7': 'Nissan has no 7 seater hydrogen vehicles available in New Zealand'
                   }

    hyundai_dict = {'BEV 5': 'Hyundai Ionic',
                    'BEV 7': 'Hyundai Kona',
                    'FCEV 7': 'Hyundai Nexo',
                    'HEV 5': 'Hyundai has no 5 seater hybrid vehicles available in New Zealand',
                    'HEV 7': 'Hyundai has no 7 seater hybrid vehicles available in New Zealand',
                    'FCEV 5': 'Hyundai has no 5 seater hydrogen vehicles available in New Zealand',
                    }

    mitsubishi_dict = {'PHEV 7': 'Mitsubishi Outlander',
                       'BEV 5': 'Mitsubishi has no 5 seater electric vehicles available in New Zealand',
                       'BEV 7': 'Mitsubishi has no 7 seater electric vehicles available in New Zealand',
                       'HEV 5': 'Mitsubishi has no 5 seater hybrid vehicles available in New Zealand',
                       'HEV 7': 'Mitsubishi has no 7 seater hybrid vehicles available in New Zealand',
                       'FCEV 5': 'Mitsubishi has no 5 seater hydrogen vehicles available in New Zealand'
                       }

    tesla_dict = {'BEV 5': 'Tesla Model 3',
                  'BEV 7': 'Tesla has no 7 seater electric vehicles available in New Zealand',
                  'HEV 5': 'Tesla has no 5 seater hybrid vehicles available in New Zealand',
                  'HEV 7': 'Tesla has no 7 seater hybrid vehicles available in New Zealand',
                  'FCEV 5': 'Tesla has no 5 seater hydrogen vehicles available in New Zealand',
                  'FCEV 7': 'Tesla has no 7 seater hydrogen vehicles available in New Zealand'
                  }

    all_brand_dict = {'HEV 5': ['Toyota Prius, Toyota Camry, Toyota Aqua, Toyota CH-R'],

                      'HEV 7': ['Toyota Rav-4, Toyota Highlander'],

                      'PHEV 5': ['Toyota Prius Prime'],

                      'PHEV 7': ['Mitsubishi Outlander'],

                      'BEV 5': ['Toyota bz4x',
                                'Nissan Leaf',
                                'Hyundai Ionic',
                                'Tesla Model 3'],

                      'BEV 7': ['Hyundai Kona'],

                      'FCEV 5': ['Toyota Mirai'],

                      'FCEV 7': ['Hyundai Nexo']
                      }


# this function will display what car model is most suited for the car based on the users specifications
def ev_model(user_key, user_brand, toyota_dict, nissan_dict, hyundai_dict, mitsubishi_dict, tesla_dict,
             all_brand_dict):
    user_ev_model = ""

    if user_brand == 'toyota':
        if user_key == 'HEV 5':
            user_ev_model = toyota_dict.get('HEV 5')
        elif user_key == 'HEV 7':
            user_ev_model =  toyota_dict.get('HEV 7')
        elif user_key == 'BEV 5':
            user_ev_model = toyota_dict.get('BEV 5')
        elif user_key == 'BEV 7':
            user_ev_model = toyota_dict.get('BEV 7')
        elif user_key == 'PHEV 5':
            user_ev_model = toyota_dict.get('PHEV 5')
        elif user_key == 'PHEV 7':
            user_ev_model = toyota_dict.get('PHEV 7')
        elif user_key == 'FCEV 5':
            user_ev_model = toyota_dict.get('FCEV 5')
        elif user_key == 'FCEV 7':
            user_ev_model = toyota_dict.get('FCEV 7')
        else:
            pass

    elif user_brand == 'nissan':
        if user_key == 'HEV 5':
            user_ev_model = nissan_dict.get('HEV 5')
        elif user_key == 'HEV 7':
            user_ev_model = nissan_dict.get('HEV 7')
        elif user_key == 'BEV 5':
            user_ev_model = nissan_dict.get('BEV 5')
        elif user_key == 'BEV 7':
            user_ev_model = nissan_dict.get('BEV 7')
        elif user_key == 'PHEV 5':
            user_ev_model = nissan_dict.get('PHEV 5')
        elif user_key == 'PHEV 7':
            user_ev_model = nissan_dict.get('PHEV 7')
        elif user_key == 'FCEV 5':
            user_ev_model = nissan_dict.get('FCEV 5')
        elif user_key == 'FCEV 7':
            user_ev_model = nissan_dict.get('FCEV 7')
        else:
            pass

    elif user_brand == 'hyundai':
        if user_key == 'HEV 5':
            user_ev_model = hyundai_dict.get('HEV 5')
        elif user_key == 'HEV 7':
            user_ev_model = hyundai_dict.get('HEV 7')
        elif user_key == 'BEV 5':
            user_ev_model = hyundai_dict.get('BEV 5')
        elif user_key == 'BEV 7':
            user_ev_model = hyundai_dict.get('BEV 7')
        elif user_key == 'PHEV 5':
            user_ev_model = hyundai_dict.get('PHEV 5')
        elif user_key == 'PHEV 7':
            user_ev_model = hyundai_dict.get('PHEV 7')
        elif user_key == 'FCEV 5':
            user_ev_model = hyundai_dict.get('FCEV 5')
        elif user_key == 'FCEV 7':
            user_ev_model = hyundai_dict.get('FCEV 7')
        else:
            pass

    elif user_brand == 'mitsubishi':
        if user_key == 'HEV 5':
            user_ev_model = mitsubishi_dict.get('HEV 5')
        elif user_key == 'HEV 7':
            user_ev_model = mitsubishi_dict.get('HEV 7')
        elif user_key == 'BEV 5':
            user_ev_model = mitsubishi_dict.get('BEV 5')
        elif user_key == 'BEV 7':
            user_ev_model = mitsubishi_dict.get('BEV 7')
        elif user_key == 'PHEV 5':
            user_ev_model = mitsubishi_dict.get('PHEV 5')
        elif user_key == 'PHEV 7':
            user_ev_model = mitsubishi_dict.get('PHEV 7')
        elif user_key == 'FCEV 5':
            user_ev_model = mitsubishi_dict.get('FCEV 5')
        elif user_key == 'FCEV 7':
            user_ev_model = mitsubishi_dict.get('FCEV 7')
        else:
            pass

    elif user_brand == 'tesla':
        if user_key == 'HEV 5':
            user_ev_model = tesla_dict.get('HEV 5')
        elif user_key == 'HEV 7':
            user_ev_model = tesla_dict.get('HEV 7')
        elif user_key == 'BEV 5':
            user_ev_model = tesla_dict.get('BEV 5')
        elif user_key == 'BEV 7':
            user_ev_model = tesla_dict.get('BEV 7')
        elif user_key == 'PHEV 5':
            user_ev_model = tesla_dict.get('PHEV 5')
        elif user_key == 'PHEV 7':
            user_ev_model = tesla_dict.get('PHEV 7')
        elif user_key == 'FCEV 5':
            user_ev_model = tesla_dict.get('FCEV 5')
        elif user_key == 'FCEV 7':
            user_ev_model = tesla_dict.get('FCEV 7')
        else:
            pass

    elif user_brand == 'all_brand':
        if user_key == 'HEV 5':
            user_ev_model = all_brand_dict.get('HEV 5')
        elif user_key == 'HEV 7':
            user_ev_model = all_brand_dict.get('HEV 7')
        elif user_key == 'BEV 5':
            user_ev_model = all_brand_dict.get('BEV 5')
        elif user_key == 'BEV 7':
            user_ev_model = all_brand_dict.get('BEV 7')
        elif user_key == 'PHEV 5':
            user_ev_model = all_brand_dict.get('PHEV 5')
        elif user_key == 'PHEV 7':
            user_ev_model = all_brand_dict.get('PHEV 7')
        elif user_key == 'FCEV 5':
            user_ev_model = all_brand_dict.get('FCEV 5')
        elif user_key == 'FCEV 7':
            user_ev_model = all_brand_dict.get('FCEV 7')
        else:
            pass

    else:
        pass

    print(user_ev_model)
    

user_ev_vehicle = ""
user_seat_number = ""
user_key = ""
user_brand = ""
toyota_dict = ""
nissan_dict = ""
hyundai_dict = ""
mitsubishi_dict = ""
tesla_dict = ""
all_brand_dict = ""

name()
information()
ev_vehicle()
car_information(user_ev_vehicle)
car_seats()
ev_key(user_ev_vehicle, user_seat_number)
brand()
brands_dict()
ev_model(user_key, user_brand, toyota_dict, nissan_dict, hyundai_dict, mitsubishi_dict, tesla_dict, all_brand_dict)

