# Uses python3
import sys

def get_change(m):
    #write your code here
    l=[10,5,1]
    change=0
    for i in l:
        change+=m//i
        m=m%i
    return change

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
