markings = input("What strange markings do you see?\n")
print()

print("Identifying...")
for position in range(0, len(markings),1):
    print(f"index {position}:", markings[position])
