import matplotlib.pyplot as plt
import random

def data():
    path={}

    a = input("""
    What type of line would you like to see?
    ':' , '--' or '-' \n
    """)

    b = input("""
    What type of colour would you like to see?
    Red - r
    Green - g or 
    Blue - b \n
    """)

    c = input("""
    What marker style would you like to see?
    'o' , 's' or '^'\n
    """)

    path['line_style'] = a
    path['color'] = b
    path['marker_style'] = c

    return path


def generate():
    line_no = int(input("How many lines would you like to display?"))

    for i in range(line_no):
        values = data()

        x = []
        for i in range(5):
            n = random.randint(1,20)
            x.append(n)

        y = []
        for i in range(5):
            m = random.randint(1,20)
            y.append(m)

    print(values.values())
    print(x,y)


generate()

