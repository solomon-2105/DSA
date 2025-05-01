class Solution:
    def myAtoi(self,s: str) -> int:
        i=0
        n=len(s)
        while i<n and s[i]==' ':
            i+=1
        if i==n:
            return 0
        sign=1
        if s[i]=='-':
            sign=-1
            i+=1
        elif s[i]=='+':
            i+=1
        num=0
        while i<n and s[i].isdigit():
            num=num*10+int(s[i])
            i+=1
        num*=sign
        num=max(-2**31,min(2**31-1,num))
        return num
