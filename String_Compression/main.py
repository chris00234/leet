class Solution:
    def compress(self, chars: List[str]) -> int:
        mp = []
        num = 1
        if len(chars) == 0:
            return 0
        
        first = chars[0]
        if len(chars) == 1:
            return len(chars)
        for i in range(1, len(chars), 1):
            if first == chars[i]:
                num += 1
            else:
                mp.append(first)
                mp.append(num)
                num = 1
                first = chars[i]
            if i == len(chars) - 1:
                if len(mp) >= 2:
                    if mp[-2] != chars[i]:
                        mp.append(chars[i])
                        mp.append(num)
                else:
                    mp.append(chars[i])
                    mp.append(num)
            

        print(mp)
        res = []
        val = 1
        for key in mp:
            if type(key) is str:
                res.append(key)
            if type(key) is int:
                val = key

            if val >= 10:
                rev = []
                while val:
                    rev.append(val % 10)
                    val = val // 10
                for i in range(len(rev) - 1, -1, -1):
                    res.append(rev[i])
            else:
                if val == 1:
                    pass
                else:
                    res.append(val)
            val = 1
        print(res)
        for i in range(len(res)):
            if type(res[i]) is int:
                res[i] = str(res[i])
            chars[i] = res[i]
                
        return len(res)
