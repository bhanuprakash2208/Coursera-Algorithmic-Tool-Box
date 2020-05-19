# Uses python3
import sys

def get_optimal_value(capacity, weight, values):
    value = 0
    proportion=[v/w for v,w in zip(values,weight)]
    # write your code here
    for _ in range(len(weights)):
        
        if capacity==0:
            return value
        max_prop=max(proportion)
        index=proportion.index(max_prop)
        proportion[index]=-1
        add_capacity=min(weight[index],capacity)
        value+=add_capacity*max_prop
        capacity-=add_capacity
        weight[index]-=add_capacity
        

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
