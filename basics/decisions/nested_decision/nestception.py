look = str(input("Where should I look?\n"))

if look == "in the bedroom":
     ask_1 = str(input("Where in the bedroom should i look?\n"))
     if ask_1 == "under the bed":
         print("Found some shoes but no battery")
     else:
         print("Found some mess but no battery")

elif look == "in the bathroom":
    ask_2 = str(input("Where in the bathroom should i look?\n"))
    if ask_2 == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery")

elif look == "in the lab":
    ask_3 = str(input("Where in the lab should i look?\n"))
    if ask_3 == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")

else:
    print("I do not know where that is but i will keep looking.")