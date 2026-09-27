class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        distToIndex = {}
        for i, (x, y) in enumerate(points):
            distance = math.sqrt((0 - x)**2 + (0 - y)**2)
            dist.append(distance)
            if distToIndex.get(distance):
                distToIndex[distance].append(i)
            else:
                distToIndex[distance] = [i]
        
        heapq.heapify(dist)
        res = []
        for i in range(k):
            distance = heapq.heappop(dist)
            index = distToIndex[distance].pop()
            res.append(points[index])

        return res