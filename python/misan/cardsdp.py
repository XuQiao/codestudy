# You have 2n cards, n red, n black, you draw cards on by one, one red pays you one dollar, one black fines you one dollar. Cards are not returned to the deck, what is the expected payoff?
import numpy as np
def payoff(n):
# 2D matrix A[r][b], denote the payoff when you have r red and b black left
# A[0][b] = 0
# A[r][0] = r
# the recursive equation is
# A[r][b] = max(0, b/(r+b) * (A[r][b-1] - 1) + r/(r+b) * (A[r-1][b] + 1))
    A = np.zeros((n,n))
    for i in range(n):
        A[i][0] = i
        A[0][i] = 0
    for r in range(1,n):
        for b in range(1,n):
            A[r][b] = max(0, 1.0*b/(r+b) * (A[r][b-1] - 1) + 1.0*r/(r+b) * (A[r-1][b] + 1))
    #print A.round(2)
    return A[n-1][n-1]

def main():
    print payoff(27)


if __name__ == '__main__':
    main()
