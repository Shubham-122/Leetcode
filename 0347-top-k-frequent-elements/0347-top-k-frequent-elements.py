class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        o=k
        m={}
        res=[]
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i]=1
        # print(m)
        sorted(m,reverse=True)
        l=m.values()
        l=list(l)
        l.sort(reverse=True)
        ref=[]
        j=0
        while(k!=0):
            ref.append(l[j])
            j+=1
            k-=1
        
        # print(ref)
        
        for i in m:
            if(o>0):
                if(m[i] in ref):
                    res.append(i)
                    o-=1
        
        return res
            
        
        