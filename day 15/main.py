
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash": 0
}

COINS ={
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.5,
    "pennies": 0.1,
}

def coffee_machine():
    #Here we play the logic of coffee machine

    def see_enough_resources(choice1, resource1):
        #See if the resources of the machine is sufficient to make to choosed coffee
        if choice1["ingredients"]["water"] > resource1["water"] or choice1["ingredients"]["milk"] > resource1["milk"] or choice1["ingredients"]["coffee"] > resource1["coffee"]:
            return False
        else:
            return True

    def payment(choice2):
        payed = 0.0
        coin =""
        coins = []
        while choice2 > payed:
            coin = input("put a coin. type 'quarter', 'dime', 'nickel', 'pennies')")
            while coin not in COINS.keys():
                coin = input("put a coin. type 'quarter', 'dime', 'nickel', 'pennies')")

            coins.append(coin)  #save the coins used in system
            payed += COINS[coin]
            print(f"you already payed ${payed}. coffee costed ${choice2} you still need pay ${choice2 - payed}")

        if choice2 != payed:
            print(f"We refund you {payed - choice2}")
            payed =payed - (payed - choice2)

        resources["cash"] += payed

    print("hello☕, which type of coffee you want to buy? (type the correspondent number")
    count = 0
    coffee ={}
    choice = ""

    for options in MENU:
        #Create the options to the client choose with numbers characters instead of type the whole number
        count += 1
        print(f"{count}- {options}")
        coffee [str(count)]  =  options

    while choice not in coffee.keys() and choice not in ["off", "report"]:
        choice = input()

    if choice == "off":
        print("Machine turn off for maintenance")
        return True

    elif choice in coffee.keys():
        if not see_enough_resources(MENU[coffee[choice]], resources):
            print("We don't have enough resources to make this coffee")
            return False

        else:
            payment(MENU[coffee[choice]]["cost"])

            resources ["water"] = resources ["water"] - MENU[coffee[choice]]["ingredients"]["water"]
            resources ["milk"] = resources ["milk"] - MENU[coffee[choice]]["ingredients"]["milk"]
            resources ["coffee"] = resources ["coffee"] - MENU[coffee[choice]]["ingredients"]["coffee"]

            print(f"here is you {coffee[choice]} Enjoy you drink!")
            return False

    elif choice == "report":
        print (resources)
        return False

end = False
while not end:

    end = coffee_machine()

