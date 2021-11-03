answer = 0


def solution(numbers, target):
    def dfs(cur, idx):
        global answer

        if idx == len(numbers):
            if cur == target:
                answer += 1
            return

        dfs(cur + numbers[idx], idx+1)
        dfs(cur - numbers[idx], idx+1)

    dfs(0, 0)
    return answer
