"""
https://www.acmicpc.net/problem/2578

구해야 하는 정답
- 사회자가 몇 번째 숫자를 부른 후 빙고가 되었는지 출력

풀이하기
- 빙고판에서 사회자가 부른 숫자의 위치를 체크하고
- 현재까지 가로, 세로, 대각선에서 빙고가 몇 개 나왔는지 체크한다

코드 설계
- input 값 받기 : 빙고판[[]], 사회자가 부르는 숫자[]
- 빙고 체크판 생성 : [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
- 사회자가 부르는 숫자가 있는 위치를 빙고판에서 찾고, 빙고 체크판에서 해당 위치의 값을 1으로 바꾸기
- 빙고 체크판에서 각각 가로, 세로, 대각선 의 합이 5가 되는지 확인
  - 합이 5가 되는 게 3개가 나오면 빙고
"""

import sys

# 5x5 빙고판 입력 받기
binggo = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]

# 사회자가 부르는 숫자 (1차원 리스트)
check = [int(i) for _ in range(5) for i in sys.stdin.readline().split()]

# 빙고 체크판 (사회자가 부르는 숫자가 해당하는 5x5 빙고판 위치에 1로 체크)
binggo_check = [[0 for _ in range(5)] for _ in range(5)]

# 빙고의 가로, 세로, 대각선을 세는 함수 정의
def binggo_check_cnt(binggo_check):
    count = 0  # 전체 빙고 개수

    sum_diagonal1 = 0  # 우상향 대각선 합
    sum_diagonal2 = 0  # 우하향 대각선 합
    
    for i in range(5):
        # 1) 가로 빙고
        if sum(binggo_check[i]) == 5:
            count += 1
        
        # 2) 세로 빙고
        """
        sum_col = 0
        for j in range(5):
            sum_col += binggo_check[j][i]
        if sum_col == 5:
            count += 1
        """
        if sum(binggo_check[j][i] for j in range(5)) == 5:
            count += 1

        # 3) 대각선 빙고
        sum_diagonal1 += binggo_check[i][4-i]  # 우상향 대각선 해당 요소값
        sum_diagonal2 += binggo_check[i][i]  # 우하양 대각선 해당 요소값
        if sum_diagonal1 == 5:
            count += 1
        if sum_diagonal2 == 5:
            count += 1

    return count
            
    
for c in range(len(check)):
    for i in range(5):
        for j in range(5):
            if check[c] == binggo[i][j]:
                binggo_check[i][j] = 1
                break 

        else:  # 루프가 break를 만나지 않고 "정상적으로 끝났을 때"만 else가 실행
            continue  
        break  # 숫자를 찾으면 i 루프도 멈추기 위해 break를 실행

    count = binggo_check_cnt(binggo_check)  # 현재까지의 빙고 개수 세기

    if count >=3:
        print(c+1)
        break