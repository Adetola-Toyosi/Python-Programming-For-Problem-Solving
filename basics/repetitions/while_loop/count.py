live_cables = int(input("How many live cables should i avoid?\n"))

no_of_live_cables = 0
print()

while no_of_live_cables < live_cables:
    print("Avoiding...", end="")
    no_of_live_cables = no_of_live_cables + 1
    print(f"Done! {no_of_live_cables} live cable avoided")
print()

print("All live cables have been avoided")
