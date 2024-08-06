class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        intervals.append(new_interval)
        intervals=sorted(intervals, key=lambda X:X[0])

        ans=[]
        curr_interval=intervals[0]
        
        for next_interval in intervals:
            if curr_interval[1]>=next_interval[0]:
                if curr_interval[1]<next_interval[1]:
                    curr_interval[1]=next_interval[1]
            else:
                ans.append(curr_interval)
                curr_interval=next_interval
        ans.append(curr_interval)

        return ans