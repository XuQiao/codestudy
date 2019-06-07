import numpy as np

def singlelane(N):
    arr = []
    for _ in np.arange(N):
        x = np.random.rand()
        arr.append(x)
    stops = N
    while stops:
        stops = 0
        for i in np.arange(N-1):
            if arr[i] > arr[i+1]:
                arr[i] = arr[i+1]
                stops = stops + 1
    return len(set(arr))

def main():
    Ntime = 10000
    arr = []
    for _ in np.arange(Ntime):
       arr.append(singlelane(100))
    print sum(arr)*1.0/Ntime
    
if __name__ == '__main__':
    main()






