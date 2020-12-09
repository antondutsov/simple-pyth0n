city = str(input().lower())
sells = float(input())

if city == "sofia":
    if 0 <= sells <= 500:
        commission = sells * 1.05
        print(f"{commission - sells:.2f}")
    elif 500 <= sells <= 1000:
        commission = sells * 1.07
        print(f"{commission - sells:.2f}")
    elif 1000 <= sells <= 10000:
        commission = sells * 1.08
        print(f"{commission - sells:.2f}")
    elif sells >= 10000:
        commission = sells * 1.12
        print(f"{commission - sells:.2f}")
    else:
        print("Error")    
elif city == "varna":
    if 0 <= sells <= 500:
        commission = sells * 1.045
        print(f"{commission - sells:.2f}")
    elif 500 <= sells <= 1000:
        commission = sells * 1.075
        print(f"{commission - sells:.2f}")
    elif 1000 <= sells <= 10000:
        commission = sells * 1.10
        print(f"{commission - sells:.2f}")
    elif sells >= 10000:
        commission = sells * 1.13
        print(f"{commission - sells:.2f}")
    else:
        print("Error")    
elif city == "plovdiv":
    if 0 <= sells <= 500:
        commission = sells * 1.055
        print(f"{commission - sells:.2f}")
    elif 500 <= sells <= 1000:
        commission = sells * 1.08
        print(f"{commission - sells:.2f}")
    elif 1000 <= sells <= 10000:
        commission = sells * 1.12
        print(f"{commission - sells:.2f}")
    elif sells >= 10000:
        commission = sells * 1.145
        print(f"{commission - sells:.2f}")
    else:
        print("Error")
else:
    print("Error")