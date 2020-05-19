# Uses python3
import sys
def get_fibonacci(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current % 10

def fibonacci_sum_naive(n):

    # Sum of n Fibonacci numbers is F(n + 2) - 1

    last_digit = get_fibonacci((n + 2) % 60)
    sum_last_digit = (last_digit - 1) if (last_digit != 0) else 9
    return sum_last_digit

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
