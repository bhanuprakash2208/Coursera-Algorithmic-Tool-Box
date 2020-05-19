def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    first=-1
    second=-1
    for i in range(n):
        if first==-1 or numbers[first]<numbers[i]:
            first=i
    for j in range(n):
        if (j!=first and (second == -1 or numbers[second]<numbers[j])):
            second=j
    return numbers[first] * numbers[second] 
        
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
