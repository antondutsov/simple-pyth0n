number = int(input())

while not (number >= 1 and number <= 100):
    print("Invalid number")
    number = int(input())
    
print(f"Valid number {number}")