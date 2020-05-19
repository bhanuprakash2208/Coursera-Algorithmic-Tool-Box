#Uses python3

import sys

def lcs2(a, b):
    T = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    for i in range(1,len(a)+1):
        
        for j in range(1,len(b)+1):
            
            if a[i-1] == b[j-1]:
                
                T[i][j] = T[i-1][j-1]+1
                
            else:
                
                T[i][j] = max(T[i][j-1],T[i-1][j])
    return T[i][j]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
