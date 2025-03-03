import sys

_ = int(sys.stdin.readline().rstrip())
nums_list = list(map(int, sys.stdin.readline().rstrip().split()))

min_num = nums_list[0]
max_num = nums_list[0] 

for i in nums_list[1:]:
    if min_num > i:
        min_num = i
    elif i > max_num:
        max_num = i

print(f"{min_num} {max_num}")