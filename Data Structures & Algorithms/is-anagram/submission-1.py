class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        if(sl!=tl): return False
        ns =sorted(s)
        nt =sorted(t)
        if(ns==nt): return True
        return False
        
        