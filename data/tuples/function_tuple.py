def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    minimum = min(likelihoods)
    maximum = max(likelihoods)
    return f"Minimum likelihood of falling: {minimum}%\nMaximum likelihood of falling: {maximum}%"

print(likelihood())