"""
https://www.acmicpc.net/problem/1181

구해야 하는 정답
- 알파벳 소문자로 이루어진 N개를 중복 없이 길이가 짧은 것부터 정렬, 길이가 같으면 사전 순으로 정렬

풀이하기
- 첫째 줄에 단어의 개수 N이 주어진다
- N개의 줄에 단어가 한 줄씩 주어진다
- 중복된 단어는 한 개만 남기고 제거한다다

코드 설계
- 입력값을 받는다 
   - 1) 단어의 개수 N
   - 2) 단어 N번 : 입력을 받을 때부터 중복을 제거하기 위해 set()에 입력값을 저장한다
- 길이 > 알파벳 순으로 정렬한다
- 결과값을 출력한다
"""

import sys

n = int(sys.stdin.readline().strip())

words_set = set()
for _ in range(n):
    words_set.add(sys.stdin.readline().strip())

result = sorted(words_set, key=lambda w: (len(w), w))
for w in result:
    print(w)