class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        m=len(word)
        k=[]
        for i in word:
            k.append(i)

        sum1=0
        sum2=0
        sum3=0
        
        
          

        for i in range(1,len(k)):
            if ord(k[i])>=65 and ord(k[i])<=90:
                sum1+=1
            elif ord(k[i])>=97 and ord(k[i])<=122:
                sum2+=1
        

        if ord(k[0])>=65 and ord(k[0])<=90:
            if sum1==m-1:
                return 1
            elif sum2==m-1:
                return 1
        else:
            if sum2+1==m:
                return 1


        

        # if sum1==m:
        #     print(sum1,'1st')
        #     return 'true'
        # elif sum2==m:
        #     print(sum2,'2nd')
        #     return 'true'
        
        



            