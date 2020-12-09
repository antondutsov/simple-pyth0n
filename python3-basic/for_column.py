print("   ",end="")
for i in range(16):
    print("%5d|"%i, end="")
print()
print(" _ _ _ _ _"*10)

for i in range(16):
    print("%5d|"%i, end="")
    
    for j in range(16):
        print("%5d|"%(i*j), end="")
    print()