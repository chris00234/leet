class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        total = 0

        for i in range(len(magazine)):
            if magazine[i] not in dic.keys():
                dic[magazine[i]] = 1
            else:
                dic[magazine[i]] += 1
        
        for i in range(len(ransomNote)):
            if ransomNote[i] in dic.keys():
                if dic[ransomNote[i]] > 0:
                    dic[ransomNote[i]] -= 1
                    total += 1
                elif dic[ransomNote[i]] == 0:
                    return False
        
        print(total)
        if total == len(ransomNote):
            return True
        return False