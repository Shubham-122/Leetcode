class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m={}
        res=[]
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        n=math.floor(len(nums)/3)
        for i in m:
            if m[i]>n:
                res.append(i)
        return res
            