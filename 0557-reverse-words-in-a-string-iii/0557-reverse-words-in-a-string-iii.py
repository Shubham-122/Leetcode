class Solution:
    def reverseWords(self, s: str) -> str:
        news=''
        s1=s.split()
        for i in s1:
            k=i[::-1]
            news=news+" "+k
        news2=''
        for i in range(1,len(news)):
            news2+=news[i]
        return news2

        