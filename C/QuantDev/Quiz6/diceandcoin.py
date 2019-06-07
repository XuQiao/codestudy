import numpy as np
import matplotlib.pyplot as plt
def throw(M, N):
    sum = 0
    for i in np.arange(M):
        x = np.random.randint(1,7)
        sum = sum + x
    for i in np.arange(N):
        x = np.random.randint(0,2)
        sum = sum + x
    return sum

def main():
    NT = 1e5
    M = 100
    N = 50
    arr = []
    for t in np.arange(NT):
        arr.append(throw(M, N))
    plt.hist(arr,bins='auto')
    plt.show()
    plt.savefig("dis.png")

if __name__ == '__main__':
    main()

