import numpy as np
# My opponent and I play a game, if I stay he quits, then I get $10 he get nothing. If both stay, we both pay $1.
def play(x, y):
    if x and y:
        return (-1, -1)
    if x and (not y):
        return (10, 0)
    if (not x) and y:
        return (0, 10)
    if (not x) and (not y):
        return (0, 0)

def main():
    N = 100000
    (moneyx, moneyy) = (0, 0)
    for _ in range(N):
        x = np.random.randint(11)<5
        y = np.random.randint(11)<5
        result = play(x, y)
        moneyx = moneyx + result[0]
        moneyy = moneyy + result[1]
    print moneyx*1.0/N, moneyy*1.0/N

if __name__ == '__main__':
    main()
