def sum_weight(weight_1, weight_2):
    total_weight = weight_1 + weight_2
    return total_weight

def calc_avg_weight(weight_1, weight_2):
    avg_weight = (weight_1 + weight_2)/2
    return avg_weight

def run():
    weight_1 = int(input("What is the weight of beep? \n"))
    weight_2 = int(input("What is the weight of bop? \n"))
    sum_of_weights = sum_weight(weight_1, weight_2)
    avg_weights = calc_avg_weight(weight_1, weight_2)

    calc = str(input("What would you like to calculate (sum or average)? \n"))

    if calc == "sum":
        print(f"The sum of Beep's and Bop's weight is {sum_of_weights}.")
    elif calc == "average":
        print(f"The average weight of Beep and Bop is {avg_weights}.")
    else:
        print("Please enter either sum or average")

run()

