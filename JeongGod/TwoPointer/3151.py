import sys
input = sys.stdin.readline

N = int(input())
students = list(map(int, input().split()))
students.sort()
ans = 0
for i in range(N-2):
    left = i+1
    right = N-1
    goal = -students[i]
    while left<right:
        tmp = students[left] + students[right]
        if tmp < goal:
            left += 1
        elif tmp > goal:
            right -= 1
        else:
            # 같은 것에서 2개를 뽑는 것 => nC2
            if students[left] == students[right]:
                k = right-left+1
                tmp = (k*(k-1))//2
                ans += tmp
                break
            # 중복이 있는지 체크한다.
            else:
                if mx_idx > right:
                    mx_idx = right
                    while mx_idx >= 0 and students[mx_idx - 1] == students[right]:
                        mx_idx -= 1
                ans += right - mx_idx + 1

                # 시간초과 난 코드
                # dup = 0
                # for idx in range(right, left, -1):
                #     if students[right] != students[idx]:
                #         break
                #     dup += 1 
                # ans += dup
            left += 1
print(ans)
