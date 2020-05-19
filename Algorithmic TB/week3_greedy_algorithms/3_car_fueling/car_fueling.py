# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    num_refills=0
    cur_refill=0
    last_refill=0
    stops.append(distance)
    while cur_refill<len(stops)-1:
        last_refill=cur_refill
        while cur_refill<len(stops)-2 and stops[cur_refill+1]-stops[last_refill]<=tank:
            cur_refill+=1
        if cur_refill==last_refill:
            return -1
        if cur_refill<len(stops)-2:
            num_refills+=1
        
    return num_refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
