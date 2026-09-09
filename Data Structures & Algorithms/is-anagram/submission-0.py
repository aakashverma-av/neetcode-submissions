class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countT, countS = {},{} # dictionary banake count kiya
        for i in range(len(s)):
            #yeh key hai, character s at index i -- yeh step hasmap banaya
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        #iterate through keys in countS
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True
        