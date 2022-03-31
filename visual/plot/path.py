import matplotlib.pyplot as plt

def coordinate():
    x = int(input('Please enter a value for x:\n'))
    y = int(input('Please enter a value for y:\n'))
    return x, y

def path():
    print("Retrieving path...")
    x_values = []
    y_values = []

    for i in range(4):
        x, y = coordinate()
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values

def run():
    values = path()
    plt.plot(values[0], values[1],'r--o')
    plt.xlabel('X values')
    plt.ylabel('Y values')
    plt.show()

run()