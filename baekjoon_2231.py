# 알고리즘 : 브루트포스(완전탐색) 

n = int(input())

for m in range(n):
    result = 0
    m = m + 1

    if n==1 or m >= n:
        print("0")
        break
    else:
        result += m
        m_list = list(map(int, str(m)))
        for each_m in m_list:
            result += each_m
        if result == n:
            print(m)
            break

""" 코드 개선
1) m 의 최소값을 찾아 탐색 범위를 줄인다. 탐색 범위는 최소 1부터 시작한다.
2) 불필요한 조건을 삭제한다.
3) 반복문의 효율을 높인다. 리스트 변환 및 반복문을 줄이고 map 객체로 변환 후 바로 더한다.
"""
n = int(input())
min_m = max(1, n-9*len(str(n)))  # 1)

for m in range(min_m, n):  # 1)
    result = m + sum(map(int, str(m)))  # 3)
    if result == n:
        print(m)
        break
else:
    print(0)