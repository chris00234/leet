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
        common = ""
        pos = 0
        min_word = 100000
        for word in strs:
            if min_word > len(word):
                min_word = len(word)
        

        for pos in range(min_word):
            if pos >= min_word:
                break
            char = word[pos]
            for w in strs:
                if char != w[pos]:
                    char = ""
            if char == "":
                break
            common += char
            # pos += 1
        return common


if __name__ == '__main__':
    ans = Solution()
    
    strs = ["flower","flow","flight"]
    
    print(ans.longestCommonPrefix(strs))