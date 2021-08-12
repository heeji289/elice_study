import sys
input = sys.stdin.readline

N = int(sys.stdin.readline())
A,B,C,D = [], [], [], []
for i in range(N):
    a,b,c,d = map(int, sys.stdin.readline().split())
    A.append(a); B.append(b); C.append(c); D.append(d);

A_B = {}
for a_num in A:
    for b_num in B:
        ab_sum = a_num + b_num
        
        if A_B.get(ab_sum) == None:
            A_B[ab_sum] = 1
        else:
            A_B[ab_sum] += 1
ans = 0
for c_num in C:
    for d_num in D:
        cd_sum = c_num + d_num
        ans += A_B.get(-(c_num + d_num), 0)

print(ans)

# 이분탐색 실패
# A_B = []
# C_D = []
# for idx1 in range(N):
#     for idx2 in range(N):
#         A_B.append(A[idx1] + B[idx2])
#         C_D.append(C[idx1] + D[idx2])
        

# C_D.sort()

# ans = 0
# visited = set()
# for num in A_B:
#     # A_B => C_D check
#     start = bisect.bisect_left(C_D, -num)
#     # -num을 찾지 못하였다면
#     if C_D[start] != -num:
#         continue
#     end = bisect.bisect_right(C_D, -num)
#     print(start, end)
#     ans += (end-start)
# print(ans)