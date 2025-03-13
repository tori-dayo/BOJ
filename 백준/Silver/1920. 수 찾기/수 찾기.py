from bisect import bisect_left, bisect_right

n = int,input()
n_array = list(map(int,input().split()))
m = int,input()
m_array = list(map(int,input().split()))

n_array.sort()

def count_num(array,x):
    left_number = bisect_left(array,x)
    right_number = bisect_right(array,x)

    if right_number - left_number > 0:
        return 1
    else:
        return 0

for i in m_array:
    print(count_num(n_array,i))