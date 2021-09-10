from collections import defaultdict


def solution(info, query):
    # 모든 경우의 수를 구함
    def dfs(_li, cnt):
        all_info.add(tuple(_li))
        
        if cnt == 4:
            return
        tmp = _li[:]
        
        dfs(tmp, cnt+1)
        tmp[cnt] = "-"
        dfs(tmp, cnt+1)
        
    
    info_list = defaultdict(list)
    for i in info:
        all_info = set()
        *rest, score = i.split()
        dfs(rest, 0)
        for j in all_info:
            info_list[j].append(score)
    
    for k in info_list:
        info_list[k].sort(key=lambda x: int(x))
    
    # score를 찾기 위한 이분탐색. 원래는 전에 효율성을 위해서 만들어둔거라 빼도 통과는 할거에요.
    # 근데 버리기 아까워서 그냥 넣었습니다.
    def binary_s(_li, target):
        start, end = 0, len(_li)-1
        while start <= end:
            mid = (start + end) // 2
            if int(_li[mid]) >= int(target):
                end = mid - 1
            else:
                start = mid + 1
        return len(_li) - (end+1)

    # query별로 돌아본다.
    ans = []
    for q in query:
        cnt = 0
        *rest, score = q.split()
        # 0 : lan, 2: job, 4: career, 6: food
        score_list = info_list[(rest[0], rest[2], rest[4], rest[6])]
        cnt = binary_s(score_list, score)

        ans.append(cnt)
    return ans
