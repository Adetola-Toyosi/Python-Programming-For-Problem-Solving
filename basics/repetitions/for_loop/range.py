level = int(input("What level of brightness is required?\n"))
print()

print("Adjusting brightness...")
print()
for i in range(2, level+2, 2):
    print("Beep's brightness level: ", end="")
    print("*"*i)
    print("Bop's brightness level: ", end="")
    print("*" * i)
    print()
print("Adjustments complete!")