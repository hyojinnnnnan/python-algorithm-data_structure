import sys, math

total_sum = 0 
num_itemType = 0
check_sum = 0 

line_check = 1
while True:
    if line_check > 2 and line_check > num_itemType:
        break

    input = sys.stdin.readline().rstrip()
    if line_check == 1:
        total_sum = int(input)
    elif line_check == 2:
        num_itemType = int(input) + 2
    else:
        item_sum = math.prod(map(int, input.split()))
        check_sum += item_sum

    line_check += 1

if total_sum == check_sum:
    print("Yes")
else:
    print("No")