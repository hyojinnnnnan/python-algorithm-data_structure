import sys

repeat = int(input())
for i in range(repeat):
    input = sys.stdin.readline().rstrip()
    print(sum(map(int, input.split())))