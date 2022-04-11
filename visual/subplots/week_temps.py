import csv
import matplotlib.pyplot as plt

file_path = 'temps.csv'


def read_data():
    temps = {}
    temps_week1 = []
    temps_week2 = []
    with open(file_path) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            temps_week1.append(row[0])
            temps_week2.append(row[1])

        temps['week 1'] = temps_week1
        temps['week 2'] = temps_week2

        return temps


def run():
    data = read_data()
    x = data['week 1']
    y = data['week 2']

    fig, axes = plt.subplots(2,1)
    axes[0].plot(x, color='g')
    axes[1].plot(y, color='r')

    plt.tight_layout()
    plt.show()

print(run())