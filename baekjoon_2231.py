n = int(input())

# 생성자 m은 분해합 n 보다 반드시 작다.
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