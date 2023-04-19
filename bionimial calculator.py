
# IMPORTS--------------------------------------------------
import matplotlib.pyplot as plt
# calculate prob = nCr * p^r * (1-p)^(n-r)
# n = total number of users
# k = number of active users
# p = the probability that a user can be active.

def prob(n, k, p):
    combination = (factorial(n) / (factorial(k) * factorial(n-k)))
    probability = combination * p**k * (1-p)**(n-k)
    return probability

# calculate factorial : n! = n * n-1 * n-2 * ....
def factorial(n):
    answer = 1
    for i in range(2, n+1):
        answer = i * answer
    return answer

# a function for drawing
def drawgraph(total, answer):
    plt.plot(total, answer, label="dots", color="purple", marker="o")
    plt.xlabel("total users")
    plt.ylabel("range of probability")
    plt.title("Binomial chart!")
    plt.legend()
    plt.show()


def main():
    all_num = int(input("The total number of users."))
    probability = float(input("The probability of being active."))
    active = int(input("The number of active users."))
    total = []
    for i in range(1, all_num+1):
        total.append(i)
    answer = []
    for i in range(1, all_num+1):
        response = prob(all_num, i, probability)
        answer.append(response)
    drawgraph(total, answer)

# call main function
main()




