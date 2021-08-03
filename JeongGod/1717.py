import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tree = [i for i in range(n+1)]
rank = [1 for i in range(n+1)]

def find(root):
    # 현재 노드가 부모노드라면
    if tree[root] == root:
        return root
    
    tree[root] = find(tree[root])
    return tree[root]

for i in range(m):
    oper, x, y = map(int, input().split())
    # 합집합
    if oper == 0:
        rx = find(x)
        ry = find(y)
        # 같은 합집합인 상태라면
        if rx == ry:
            continue
        # 합치는데 rank를 기준으로 합친다.
        if rank[rx] < rank[ry]:
            tree[rx] = ry
        else:
            tree[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

    # 집합안에 있는지 출력
    else:
        rx = find(x)
        ry = find(y)

        print("YES" if rx == ry else "NO")
