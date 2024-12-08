import sys

rows, cols = map(int, sys.stdin.readline().rstrip().split())

first_array = []
second_array = []

for _ in range(rows):
    first_array.append(list(map(int, sys.stdin.readline().rstrip().split())))
for _ in range(rows):
    second_array.append(list(map(int, sys.stdin.readline().rstrip().split())))

''' 입력을 분리하여 코드를 조금 더 간결하게 작성
for i in range(2):
    for row in range(rows):
        input = list(map(int, sys.stdin.readline().rstrip().split()))
        if i == 0:
            first_array.append(input)
        else:
            second_array.append(input)
'''
for row in range(rows):
    result_rows = [first_array[row][col] + second_array[row][col] for col in range(cols)]
    print(' '.join(map(str, result_rows)))

''' 문자열 누적 방식 대신, 리스트 컴프리헨션과 join을 사용하여 출력 
for row in range(rows):
    print_str = ''
    for col in range(cols):
        output_sum = first_array[row][col] + second_array[row][col]
        print_str += str(output_sum) + ' '
    print(print_str.rstrip())
'''