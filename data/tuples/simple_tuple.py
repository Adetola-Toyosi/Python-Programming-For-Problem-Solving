def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)

def run():
    store = likelihood()
    return f"Minimum likelihood of falling: {store}%"

# if __name__ == "__main__":
#     run()
print(run())

