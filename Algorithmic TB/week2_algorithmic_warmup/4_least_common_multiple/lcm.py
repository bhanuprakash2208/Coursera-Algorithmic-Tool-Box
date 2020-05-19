# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
def lcm_naive(a, b):
    return (a*b)//gcd(a,b)


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

