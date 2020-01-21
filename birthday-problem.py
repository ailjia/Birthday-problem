def prob(n):
    """
    :param n: the number of people in the room
    :return: the probability that all birthday in the room are different
    """
    if n == 1:
        return 1
    else:
        return (1 - (n-1) / 365.0) * prob(n-1)  # In order to make this a float division,  convert 365 into a float.

n = int(input('how many people are there in the room?')) # Convert the default strings into integer
birthday_prob = 1 - prob(n) # the probability that at least two people have the same birthday
print(birthday_prob)