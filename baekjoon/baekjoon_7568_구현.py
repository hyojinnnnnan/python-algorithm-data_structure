"""
https://www.acmicpc.net/problem/7568

구해야 하는 정답

풀이하기

코드 설계

"""
########################### 제출 1
import sys
N = int(sys.stdin.readline().strip())

info = []
for _ in range(N):
    info.append(list(map(int, sys.stdin.readline().split())) + [0])  # [몸무게, 키, 나보다 큰 사람]

for i in info:
    current_w = i[0]  # 몸무게
    current_h = i[1]  # 키
    current_bigP = i[2]  # 나보다 큰 사람

    for j in info:
        other_w = j[0]  # 몸무게
        other_h = j[1]  # 키

        if current_w < other_w and current_h < other_h:
            current_bigP += 1
    
    i[2] = current_bigP + 1


print(" ".join(str(row[2]) for row in info))
#print(" ".join(map(str, [row[2] for row in info])))


########################### 제출 2
"""
1. 리스트 컴프리헨션을 사용한 데이터 입력
  - 기존 리스트를 수정하지 않고, N개의 리스트를 한 번에 생성하여 `info` 에 할당
    - 한 번의 연산으로 리스트를 생성하기 때문에 [제출 1] 보다 빠름

  - 제출 1의 방식은 `info` 리스트를 먼저 생성한 후, `append()` 를 사용하여 값을 하나씩 추가
    - 리스트를 매번 업데이트하는 방식 (기존 리스트 수정)
    - `append()` 는 `O(1)` 이므로 개별 추가 비용은 낮지만, 전체적으로는 N번 실행됨

2. `+ [1]` 연산 을 통한 리스트 확장 대신 `.append(1)` 를 통해 리스트 직접 수정
  - `+` 연산: 새로운 리스트를 만들어 기존 리스트와 결합
  - `append()`: 기존 리스트에 요소 추가

3. 불필요한 변수 제거 (current_w, current_h 제거)
  - 직접 참조하도록 변경하여 변수 제거

4. `if i != j` 조건 추가하여 자기 자신 비교 방지 (반복문 내에서 비교 횟수 감소)
"""
import sys
N = int(sys.stdin.readline().strip())

info = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]  # 1

for i in range(len(info)):
    info[i].append(1)  # 2
    for j in range(len(info)):
        if i!=j and (info[i][0] < info[j][0] and info[i][1] < info[j][1]):  # 3, 4
            info[i][2] += 1

print(" ".join(str(i[2]) for i in info))