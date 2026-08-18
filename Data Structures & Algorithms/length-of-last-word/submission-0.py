class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = int(len(s))
        b = a - 1
        print(a)
        temp = ""
        if(s[b] == " "):
            s = s.strip()
        for i in s:
            if(i == " "):
                 temp = ""
                 print(temp)
            else:
                temp+= i
                print(temp)
        
        return(len(temp))

  
        