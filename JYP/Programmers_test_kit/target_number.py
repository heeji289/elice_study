'''
풀이 1 - 이진 탐색 트리는 아니지만 계산 결과를 층으로 나누어 누적합 계산하기
- 질문 게시판 참고했습니다;
- 현재 레이어(배열)에 존재하는 값에 다음에 오는 숫자를 더하고 빼서 추가
- 예 : numbers = [1, 2, 3] 
                    1
            1+2         1-2 
    1+2+3   1+2-3       1-2+3   1-2-3
- 다음 레이어에 있는 원소 개수는 이전 레이어의 원소 개수보다 2배씩 증가함
- 최종 레이어에 존재하는 값에서 원하는 target이 있는지 여부를 카운트하기

'''

def solution(numbers, target):

    answer = 0
    curr_layer = []

    for idx in range(len(numbers)):
        
        next_layer = []
        next_num = numbers[idx]
        if idx == 0:
            curr_layer.append(numbers[idx])
            curr_layer.append(-numbers[idx])
        else:
            for curr_num in curr_layer:
                next_layer.append(curr_num + next_num)
                next_layer.append(curr_num - next_num)

            curr_layer = next_layer
    
    answer = curr_layer.count(target)

    return answer

'''
풀이 2 - 이진트리 생성 후 dfs 수행(실패)
...결과를 보니 뭔가 이상함
'''

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root):
        self.root = root
    
    def insert(self, val):
        self.root = self._insert_val(self.root, val)
        return self.root is not None

    def _insert_val(self, node, data):
        if node is None:
            node = Node(data)
        else:
            node.left = self._insert_val(node.left, data)
            node.right = self._insert_val(node.right, (-1)*data)
        
        return node

    
    global nums
    nums = []
    
    def preorder(self, n):
        if n != None:        
            nums.append(n.data)
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)




def solution(numbers, target):
    
    tree=BinaryTree(Node(0))

    for num in numbers:
        tree.insert(num)
    
    tree.preorder(tree.root)

    len_n = len(numbers)
    answer = 0

    for i in range(1, len(nums) - len_n, len_n):
        print(nums[i:i+len_n])
        if sum(nums[i:i+len_n]) == target:
            answer += 1
    
    print(len(nums))
    return answer

'''
