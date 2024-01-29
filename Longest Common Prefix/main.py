"""
    Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
"""

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        length = 200
        for w in strs:
            if length > len(w):
                length = len(w)
        
        result = ""
        ind = 0
        same = False
        for ind in range(length):
            letter = strs[0][ind]
            for word in strs:
                if letter == word[ind]:
                    same = True
                else:
                    same = False
            if same == True:
                result += letter
        return result


if __name__ == '__main__':
    ans = Solution()
    
    strs = ["flower","flow","flight"]
    
    print(ans.longestCommonPrefix(strs))