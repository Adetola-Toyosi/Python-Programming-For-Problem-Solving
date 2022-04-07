import matplotlib.pyplot as plt


def read_data(file_path):  # created function to read the file path
    with open(file_path, 'r') as file:
        file_list = []
        for line in file:
            file_list.append(int(line.strip()))
    return file_list


def run():
    data = read_data('temps.txt')  # returns function by reading file path

    fig, axis = plt.subplots(1, 2)  # to plot two subplots, side-by-side

    axis[0].plot(data, color='g')  # line graph
    axis[0].set_xlabel('Temperatures')
    axis[0].set_title('Line graph showing temperatures', fontstyle='italic')

    axis[1].bar(range(len(data)), data, color='b')  # bar graph
    axis[1].set_xlabel('Temperatures')
    axis[1].set_title('Bar graph showing temperatures', fontstyle='italic')

    plt.tight_layout()
    plt.show()


print(run())

