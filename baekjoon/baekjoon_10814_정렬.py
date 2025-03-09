"""
https://www.acmicpc.net/problem/10814

구해야 하는 정답
- 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬

풀이하기
- 첫번째 입력값으로 회원 수가 주어진다
- 회원 수만큼 반복해서 이름과 나이 값을 받는다
- 입력한 순서가 가입 순서다

코드 설계
- 첫번째 입력값을 받는다
- 첫번째 입력값의 수 만큼 반복하여 입력값을 받는다 : [(입력된 순서, 나이, 이름)]
  - 튜플과 리스트는 비슷하지만, 튜플은 "변경 불가능(immutable)"한 자료형
  - 데이터 변경을 방지하고 속도를 향상시키기 위해 [[]] 대신 [()] 로 사용
- 나이를 기준으로 오름차순 정렬을 한다
- 나이가 같으면 가입 순서대로 오름차순 정렬을 한다
"""

import sys

member_num = int(sys.stdin.readline().strip())

member_info = []
for i in range(member_num):
    info = sys.stdin.readline().strip().split()
    member_info.append((i, int(info[0]), info[1]))

member_info = sorted(member_info, key=lambda member: (member[1], member[0]))
print("\n".join(map(lambda member: f"{member[1]} {member[2]}", member_info)))