def observed():
    observations = []

    for i in range(5):
        answer = input("Please enter an observation: \n")
        observations.append(answer)

    return observations


def remove_observations(observations_list):
    answer = input("Do you want to remove an observation (yes/no)?\n")
    while answer == "yes":
        observation_to_remove = input("What observation do you wish to remove?\n")
        observations_list.remove(observation_to_remove)
        print(f"Done!\n{observation_to_remove} has been removed from your list of observations")

        answer = input("Do you still want to remove an observation (yes/no)?\n")


def run():
    observations = observed()
    remove_observations(observations)

    set_of_observations = set()
    for value in observations:
        data = (value, observations.count(value))
        set_of_observations.add(data)

    for data in sorted(set_of_observations):
        print(f"{data[0]} observed {data[1]} times.")


run()