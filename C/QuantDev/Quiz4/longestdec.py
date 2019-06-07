def main():
    def longestdes(array):
        n = len(array)
        if n == 1:
            return array
        maxsize = 0
        currsize = 0
        for i in range(n):
            if i < n - 1:
                if array[i + 1] < array[i]:
                    currsize = currsize + 1
                else:
                    currsize = 0
                if currsize > maxsize:
                    maxsize = currsize
                    pos = i + 1
            if maxsize == 0:
                pos = 0
        print pos, maxsize
        return array[pos-maxsize:pos+1] # subarray size is maxsize + 1
    array = [11, 5, 7, 9, 2, 0, -3, 3]
    l = longestdes(array)
    print array
    print l #[9, 2, 1, 0]


if __name__ == '__main__':
    main()
