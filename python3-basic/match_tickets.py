budget = float(input())
tickets = input().lower()
people = int(input())

if tickets == "normal":
    tickets = 249.99
elif tickets == "vip":
    tickets = 499.99
else:
    print("enter ticket")

if 1 <= people <= 4:
    transport = (budget * 0.75)
elif 5 <= people <= 9:
    transport = (budget * 0.60)
elif 10 <= people <= 24:
    transport = (budget * 0.50)
elif 25 <= people <= 49:
    transport = (budget * 0.40)
elif people >= 50:
    transport = (budget * 0.25)
else:
    print("enter number of people")

budget_left = budget - (transport + people * tickets)

if budget_left >= 0:
    print(f"Yes! You have {budget_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget_left):.2f} leva.")