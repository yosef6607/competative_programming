class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance=list()
        ans=list()
        for i in range(len(points)):
            distance.append((math.sqrt(points[i][0]**2 +points[i][1]**2),points[i]))
        distance.sort()
        for j in range(k):
            ans.append(distance[j][1])
        return ans
        
