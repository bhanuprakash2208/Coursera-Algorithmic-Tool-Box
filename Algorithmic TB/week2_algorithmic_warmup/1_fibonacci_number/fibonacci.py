# Given code
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)
# Modified code
def calc_fib(n):
    if (n <= 1):
        return n
    f=[0]*(n+1)
    f[1]=1
    for i in range(2,n+1):
        f[i]=f[i-1]+f[i-2]
    return f[n]


n = int(input())
print(calc_fib(n))
