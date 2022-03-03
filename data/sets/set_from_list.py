def observed():
    observations = []

    for i in range(7):
        answer = str(input("Please enter an observation: \n"))
        observations.append(answer)

    return observations


def run():
    print("Counting observations...")
    store = observed()

    set_of_observations = set()
    for value in store:
        data = (value, store.count(value))
        set_of_observations.add(data)

    for value in set_of_observations:
        print(f"{value[0]} observed {value[1]} times.")

run()
