fruit = input().lower()
day = input().lower()
quantity = float(input())
price = -1.0
if(day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday"):
    if fruit == "banana":
        price = quantity * 2.50
    elif fruit == "apple":
        price = quantity * 1.20
    elif fruit == "orange":
        price = quantity * 0.85
    elif fruit == "grapefruit":
        price = quantity * 1.45
    elif fruit == "kiwi":
        price = quantity * 2.70
    elif fruit == "pineapple":
        price = quantity * 5.50
    elif fruit == "grapes": 
        price = quantity * 3.85
        
elif (day == "sunday" or day == "saturday"):
    if fruit == "banana":
        price = quantity * 2.70
    elif fruit == "apple":
        price = quantity * 1.25
    elif fruit == "orange":
        price = quantity * 0.90
    elif fruit == "grapefruit":
        price = quantity * 1.60
    elif fruit == "kiwi":
        price = quantity * 3.00
    elif fruit == "pineapple":
        price = quantity * 5.60
    elif fruit == "grapes":     
        price = quantity * 4.20
    
if price >= 0:
    print(f"{price:.2f}")
else:
    print("error")
