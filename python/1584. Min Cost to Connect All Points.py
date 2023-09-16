from typing import List

def minCostConnectPoints(points: List[List[int]]) -> int:
    def manhattan_distance(p1: List[int], p2: List[int]) -> int:
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    plen = len(points)
    # edges
    edges = []
    for i in range(plen):
        for j in range(i+1,plen):
            edges.append([manhattan_distance(points[i],points[j]),i,j])
    edges.sort() # sort edges
    
    parent = list(range(plen))
    def search(x: int):
        if x != parent[x]:
            return search(parent[x])
        return x

    ans = 0
    for dist, i, j in edges:
        p1 = search(i)
        p2 = search(j)
        if p1 != p2:
            ans += dist
            parent[p1] = p2
    return ans

if __name__ == "__main__":
    print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))  # Expected output: 20
    print(minCostConnectPoints([[3,12],[-2,5],[-4,1]]))  # Expected output: 18
    print(minCostConnectPoints([[2,-3],[-17,-8],[13,8],[-17,-15]]))  # Expected output: 53
