import sys

total_list = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
extra_nums = sum(total_list) - 100

flag = False
for idx in range(9):
    except_num1 = total_list[idx]

    for next_idx in range(idx+1, 9):
        except_num2 = total_list[next_idx]
    
        if extra_nums == except_num1 + except_num2:
            total_list.remove(except_num1)
            total_list.remove(except_num2)
            flag = True
            break

    if flag == True:
        break

sorted_total_list = sorted(total_list)
for n in sorted_total_list:
    print(n)