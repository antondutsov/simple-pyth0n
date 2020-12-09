width = int(input())
lenght = int(input())
height = int(input())
decore = float(input())

volume = width * lenght * height * 0.001
decore = decore * 0.01
liters = volume * (1 - decore)
print(f"{liters:.3f}")