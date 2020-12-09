num_of_day = int(input())

if 1 <= num_of_day <= 7:
    if num_of_day == 1:
        print("Monday")
    elif num_of_day == 2:
        print("Tuesday")
    elif num_of_day == 3:
        print("Wednesday")
    elif num_of_day == 4:
        print("Thursday")
    elif num_of_day == 5:
        print("Friday")
    elif num_of_day == 6:
        print("Saturday")
    elif num_of_day == 7:
        print("Sunday")
else:
    print("Error")