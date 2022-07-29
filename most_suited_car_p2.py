# most suited car program
"""I will construct a program that will calculate which type of energy efficient car is most suited for the user
    according to their requirements and specifications"""

import emoji


# this function will ask the user for their name
def name():
    user_name = input("What is your name?")
    print(emoji.emojize("Hello {} :smiling_face:".format(user_name)))


# this function will inform the user about energy efficient cars
def information():
    user_information = input(
        "Do you want background information about energy efficient cars?"
        "Please enter yes / y or no / n"
    ).lower

    if user_information == "yes" or "y":
        print(
            "Energy efficient cars are also known as clean cars and the government of New Zealand reduces the price of "
            "energy efficient cars using a clean car rebate of up to $8,625. Energy efficient cars are cars that "
            "consume less or no petrol to reduce carbon emissions released by the vehicle. Reducing carbon emissions "
            "decreasing greenhouse gases that increase the temperature of Earth, causing climate change. "
            "This program will ask you for your requirements to show the most suited  "
        )

    elif user_information == "no" or "n":
        pass

    else:
        print("Please enter yes / y or no / n")


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


# this function will calculate what type of energy efficient car is most suited for the user
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

        return user_ev_vehicle

    print("The most suited type of energy efficient car for you is {}".format(user_ev_vehicle))


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

    elif user_ev_vehicle == "plug-in hybrid":
        print(
            "Plug-in hybrid electric vehicles (PHEVs) are powered by an internal combustion engine in "
            "combination with one or more electric motors that use energy stored in batteries. In a PHEV, the "
            "extra power provided by the electric motor may allow for a smaller combustion engine. The vehicle uses "
            "regenerative braking and the internal combustion engine to charge internally. The vehicle captures "
            "energy normally lost during braking by using the electric motor as a generator and storing the captured "
            "energy in the battery. These batteries can be externally charged, similar to an electric car (BEVs)"
            "allowing more range than the average hybrid electric vehicle (HEVs)"
        )

    elif user_ev_vehicle == "electric":
        print(
            "Electric cars (BEVs) are powered by energy from the battery. These batteries can be externally charged. "
            "This energy is converted into power by an electric motor, which is used to drive the wheels."
        )

    elif user_ev_vehicle == "hydrogen":
        print(
            "Hydrogen cars (FCEVs) are powered by hydrogen which enter the fuel cell from a tank and mix with oxygen "
            "to create water (H2O) in a chemical reaction, the water if released from the exhaust pipe which generates "
            "electricity that is used to power the motors that drive the wheels."
        )

    else:
        pass


# this function will have a list of cars from brands
def brands_list():
    toyota_dict = {['Toyota Prius, '
                    'Toyota Camry, '
                    'Toyota CH-R']: 'HEV 5',
                   ['Toyota Rav-4, '
                    'Toyota Highlander']: 'HEV 7',
                   'Toyota Prius Prime': 'PHEV 5',
                   'Toyota Mirai': 'FCEV 5',
                   'Toyota bz4x': 'BEV 5',
                   'Toyota has no 7 seater electric vehicles available in New Zealand': 'BEV 7'
                   }
    toyota_valid_dict = {['Toyota Prius, '
                          'Toyota Camry, '
                          'Toyota CH-R']: 'HEV 5',
                         ['Toyota Rav-4, '
                         'Toyota Highlander']: 'HEV 7',
                         'Toyota Prius Prime': 'PHEV 5',
                         'Toyota Mirai': 'FCEV 5',
                         'Toyota bz4x': 'BEV 5',
                         }
    nissan_dict = {'Nissan Leaf': 'BEV 5',
                   'Nissan has no 7 seater electric vehicles available in New Zealand': 'BEV 7',
                   'Nissan has no 5 seater hybrid vehicles available in New Zealand': 'HEV 5',
                   'Nissan has no 7 seater hybrid vehicles available in New Zealand': 'HEV 7',
                   'Nissan has no 5 seater hydrogen vehicles available in New Zealand': 'FCEV 5',
                   'Nissan has no 7 seater hydrogen vehicles available in New Zealand': 'FCEV 7'
                   }
    nissan_valid_dict = {'Nissan Leaf': 'BEV 5'
                         }
    hyundai_dict = {'Hyundai Ionic': 'BEV 5',
                    'Hyundai Kona': 'BEV 7',
                    'Hyundai Nexo': 'FCEV 7',
                    'Hyundai has no 5 seater hybrid vehicles available in New Zealand': 'HEV 5',
                    'Hyundai has no 7 seater hybrid vehicles available in New Zealand': 'HEV 7',
                    'Hyundai has no 5 seater hydrogen vehicles available in New Zealand': 'FCEV 5',
                    }
    hyundai_valid_dict = {'Hyundai Ionic': 'BEV 5',
                          'Hyundai Kona': 'BEV 7',
                          'Hyundai Nexo': 'FCEV 7'
                          }
    mitsubishi_dict = {'Mitsubishi Outlander': 'PHEV 7',
                       'Mitsubishi has no 5 seater electric vehicles available in New Zealand': 'BEV 5',
                       'Mitsubishi has no 7 seater electric vehicles available in New Zealand': 'BEV 7',
                       'Mitsubishi has no 5 seater hybrid vehicles available in New Zealand': 'HEV 5',
                       'Mitsubishi has no 7 seater hybrid vehicles available in New Zealand': 'HEV 7',
                       }
    mitsubishi_valid_dict = {'Mitsubishi Outlander': 'PHEV 7'
                             }
    tesla_dict = {'Tesla Model 3': 'BEV 5',
                  'Tesla has no 7 seater electric vehicles available in New Zealand': 'BEV 7',
                  'Tesla has no 5 seater hybrid vehicles available in New Zealand': 'HEV 5',
                  'Tesla has no 7 seater hybrid vehicles available in New Zealand': 'HEV 7',
                  'Tesla has no 5 seater hydrogen vehicles available in New Zealand': 'FCEV 5',
                  'Tesla has no 7 seater hydrogen vehicles available in New Zealand': 'FCEV 7'
                  }
    tesla_valid_dict = {'Tesla Model 3': 'BEV 5'
                        }
    lexus_dict = {''
                  }
    lexus_valid_dict = {''
                        }
    kia_dict = {''
                }
    kia_valid_dict = {''
                      }
    all_brand_list = {toyota_valid_dict +
                      nissan_valid_dict +
                      hyundai_valid_dict +
                      mitsubishi_valid_dict +
                      tesla_valid_dict +
                      lexus_valid_dict +
                      kia_valid_dict}


# this function will ask the user if they are looking for a specific brand
def brand():
    valid_brands_list = ['toyota', 'nissan', 'hyundai', 'mitsubishi', 'tesla', 'lexus', 'kia']
    user_brand = input("Are you looking for a specific brand?"
                       "Please enter yes / y or no / n").lower

    if user_brand == "yes" or user_brand ==  "y":
        car_brand = input("What brand are you looking for?").lower
        for car_brand in valid_brands_list:
            pass
        else:
            print("the brand you have entered is a typo or not in the list of brands due to not enough energy "
                  "efficient car models")
    elif user_brand == "no" or user_brand == "n":
        pass


# this function will ask the user if they are looking for a 5-seater or a 7-seater
def car_seats():
    user_seat_number = int(input("Are you looking for a 5-seater or a 7-seater?"
                                 "Please enter '5' or '7'"))
    if user_seat_number == "5":
        pass
    elif user_seat_number == "7":
        pass
    else:
        print("Please enter '5' or '7'")

    return user_seat_number


# this function will display what car model is most suited for the car based on the users specifications
def ev_model(user_ev_vehicle, brands_list, brand):
    if user_ev_vehicle == "hybrid" and user_ev_vehicle == "5":
        print

