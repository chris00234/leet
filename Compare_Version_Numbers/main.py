class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        n = len(v1) if len(v1) < len(v2) else len(v2)
        pos = 0
        for i in range(n):
            if int(v1[i]) < int(v2[i]):
                return -1
            if int(v1[i]) > int(v2[i]):
                return 1
            pos += 1
        
    
        if len(v1) > len(v2):
            while pos < len(v1):
                if int(v1[pos]) > 0:
                    return 1
                pos += 1
        elif len(v2) > len(v1):
            while pos < len(v2):
                if int(v2[pos]) > 0:
                    return -1
                pos += 1

        return 0
