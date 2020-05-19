import sys
def pisano(m): 
    previous, current = 0, 1
    for i in range(1, m * m): 
        previous, current = current, (previous + current) % m 
        if (previous == 0 and current == 1): 
            return i


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    n = n % pisano(m)

    previous = 0
    current  = 1
    if n==0: 
        return 0
    elif n==1: 
        return 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
