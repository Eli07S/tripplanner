# Eli.S
# Sep 8, 2023

def intro_data():
    global FirstName
    global LastName
    global Destination
    global TravelDays
    global intdaystravled
    global Budget
    global fltbudget
    global CurrencySymbol
    global Conversion
    print ("Hello, welcome to my trip planner program")
    FirstName = input ("What is you First Name ")
    LastName = input ("What is you Last Name ")
    print ("Hi! "+ FirstName + ' ' + LastName)
    Destination = input ("Where do you want to go? ")
    print ("Great Choice!")
    # Travel time
    TravelDays = input ("How many days are you planning to travel? ")
    intdaystravled = int(TravelDays)
    Budget = input ("What is your budget for this trip in USD? ")
    fltbudget = float(Budget)
    CurrencySymbol = input ("What is the currency symbol at your destination? ")
    Conversion = float(input ("What is the conversion rate from USD to " + CurrencySymbol + " "))
intro_data()

def converter():
    HoursTraveled = int(TravelDays) * 24
    MinutesTraveled = int(HoursTraveled) * 60
    SecondsTraveled = int(MinutesTraveled) * 60
    print ("You will be traveling a total of" , HoursTraveled , "Hours" , MinutesTraveled , "minutes, and" , SecondsTraveled , "seconds ")

    # Budget per day
    print ("your total budget for the trip is" , Budget)
    DailyBudget = fltbudget/intdaystravled
    roundailybudget = round(DailyBudget,2)
    print ("Your budget per day is" , roundailybudget,"USD")

    # Budget in Destination Country
    destinationcurrency = fltbudget * Conversion
    print (destinationcurrency , CurrencySymbol, "this is the conversion rate from USD to " + CurrencySymbol)
converter()

def valid_check():
    try:
        intro_data()
        converter()
    except:
        print("Error: make sure input is in the proper format")
        valid_check()
valid_check()

def timedifference():
    TimeDifference = int(input("please provide the time differnce, of your destinations, if time zone is behind, please provide a negative number "))
    TimeChange = (TimeDifference + 12) % 24
    print ("when it is twelve O'clock at home it is, " ,TimeChange, ":00 at your destination")
timedifference()

def Countryarea():
    CountryArea = input ("Please enter the size of your destination in square kilometers")
    try:
        CountryArea = float(CountryArea)
    except:
        print("Check for proper format")
        CountryArea()
    roundedcountryarea = CountryArea * 0.386102
    print ("The area of travel of your country is" , int(roundedcountryarea) , "square miles")
Countryarea()