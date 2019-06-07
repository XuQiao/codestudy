import matplotlib.pyplot as plt
import numpy as np
import reg

def main():
    prices = []
    with open("output.txt") as f:
        f.readline()
        for line in f:
            Id, position, price, size = line.split(' ')
            print prices
            prices.append(price)

    plt.hist(price, bins = 'auto')
    plt.draw()

if __name__ == '__main__':
    main()


