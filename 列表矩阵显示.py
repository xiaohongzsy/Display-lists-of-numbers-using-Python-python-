print(format("Multiplication Table",">30s"))

print(" ",end="")

for i in range(1,10):
    print(" ",i,end="")

print()

print("-"*30)

for i in range(1,10):
    print(i,"|",end="")
    for j in range(1,10):
        print(format(i*j,"4d"),end="")
    print()











