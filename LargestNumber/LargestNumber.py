class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        res = list()
        list1 = permutations(nums,len(nums))
        for i in list1:
            res.append(int(''.join(map(str, i))))
        return str(max(res))


        
        
