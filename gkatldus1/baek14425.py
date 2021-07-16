import sys
input = sys.stdin.readline

N, M= map(int, input().split())         
N_put = set()       # set으로 N만큼 문자열을 받은 후, M만큼 문자열이 들어올때마다 각각 N에 같은 문자열이 있는지 확인해준다.
cnt = 0
for i in range(N):
    N_put.add(input().strip())
for i in range(M):
    M_input = input().strip()
    if M_input in N_put:
        cnt += 1
print(cnt)