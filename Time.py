def greet():
    hour = int(input("Please enter the hour (1-12): "))
    minute = int(input("Please enter the minutes (0-59): "))
    period = input("Is it AM or PM? ").strip().upper()

    if period == "PM" and hour != 12:
        hour += 12
    if period == "AM" and hour == 12:
        hour = 0
    
    if 5 < hour <= 12:
        greeting = "Good Morning"
    elif 12 < hour <= 16:
        greeting = "Good Afternoon"
    elif 16 < hour <= 20:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    print("The time you entered is {:02d}:{:02d}.".format(hour, minute), greeting)

greet()
