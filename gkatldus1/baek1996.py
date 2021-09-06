import sys
input = sys.stdin.readline

repeat = int(input())

for _ in range(repeat):
    N,M = map(int, input().split())
    nums = [int(x) for x in input().split()]    #입력 받는 값
    idx = [i for i in range(len(nums))]         #M의 위치를 추적하기 위한 인덱스 리스트
    idx[M] = 'target'                           #M위치의 인덱스를 target으로 바꿔줌

    
    cnt = 0
    
    while True:
        
        if nums[0]==max(nums):          #리스트의 첫번째 위치에 가장 큰 값이 올 경우 카운트를 올려주고, 
                                        #이 값이 타겟이라면 루프를 끝냄. 타겟이 아니라면 인덱스 리스트와 받은 값 리스트에서 빼준다.
            cnt += 1
                        
            
            if idx[0]=='target':
                print(cnt)
                break
            else:
                nums.pop(0)
                idx.pop(0)

        else:                           #리스트의 첫번째 위치에 가장 큰 값이 아닐 경우 큐에서 값을 빼고 다시 넣어준다.
            nums.append(nums.pop(0))
            idx.append(idx.pop(0))  
