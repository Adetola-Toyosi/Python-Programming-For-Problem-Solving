def display_ladder(steps):
    return"""
    | |
    ***
    """ *steps

def create_ladder():
    num_steps = int(input("How many steps remain? \n"))
    return display_ladder(num_steps)

print(create_ladder())


