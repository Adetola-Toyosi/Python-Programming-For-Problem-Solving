bars = int(input("How many bars should be charged?\n"))
print()

no_of_bars = 0
while no_of_bars < bars:
    print("Charging: ", end="")
    no_of_bars = no_of_bars + 1
    print("█ " * no_of_bars)
print()
print("The battery is fully charged")