class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water=0
        l=0
        r=len(height)-1
        while(l<r):
            hl,hr=height[l],height[r]
            curr_water=min(hl,hr)*(r-l)
            if curr_water>max_water:
                max_water=curr_water
            if hl<=hr:
                l+=1
            if hl>=hr:
                r-=1
        return max_water