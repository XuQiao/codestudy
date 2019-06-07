import numpy as np
import matplotlib.pyplot as plt

def fill():
    sum = 0
    result = 0
    while(sum < 1):
        cup = np.random.uniform()
        sum = sum + cup
        result = result + 1
    return result

def main():
    N = 1000000
    arr = list()
    for _ in range(N):
        res = fill()
        arr.append(res)
    arr3 = [i for i in arr if i == 5]
    print len(arr3)*1.0/len(arr)
    plt.hist(arr,bins='auto')
    plt.show()

if __name__ == '__main__':
    main()
