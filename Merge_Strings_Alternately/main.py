class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        merged = ""
        pos = 0
        if length1 >= length2:
            for i in range(length2):
                merged += word1[i]
              
                merged += word2[i]
                pos += 1
                
            # pos += 1
            for j in range(pos, length1):
                merged += word1[j]
               
            
        else:
            for i in range(length1):
                merged += word1[i]
                
                merged += word2[i]
                pos += 1
             
            # pos += 1
            for j in range(pos, length2):
                merged += word2[j]
                
            
        return merged
