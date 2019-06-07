def matrixrot(matrix):
    m = len(matrix)
    n = len(matrix[0])
    results = []
    for i in range(n):
        rows = []
        for j in range(m):
            rows.append(matrix[j][i])
        results.append(rows)

    return results

if __name__ == '__main__':
    print(matrixrot([[0,1,2,3],[2,3,4,5],[2,6,1,6]]))
