product = input()
city = input()
quantity = float(input())

result = None

if city.lower() == "sofia":
    if product == "coffee":
        result = quantity * 0.5
    elif product == "water":
        result = quantity * 0.8
    elif product == "beer":
        result = quantity * 1.20
    elif product == "sweets":
        result = quantity * 1.45
    elif product == "peanuts":
        result = quantity * 1.65
    else:
        print()    
else:
    print()
        
if city.lower() == "plovdiv":
    if product == "coffee":
        result = quantity * 0.40
    elif product == "water":
        result = quantity * 0.70
    elif product == "beer":
        result = quantity * 1.15
    elif product == "sweets":
        result = quantity * 1.30
    elif product == "peanuts":
        result = quantity * 1.50
    else:
        print()
else:
    print()
        
if city.lower() == "varna":
    if product == "coffee":
        result = quantity * 0.45
    elif product == "water":
        result = quantity * 0.70
    elif product == "beer":
        result = quantity * 1.10
    elif product == "sweets":
        result = quantity * 1.35
    elif product == "peanuts":
        result = quantity * 1.55    
    else:
        print()
else:
    print()


print(f"{result:.3f}")