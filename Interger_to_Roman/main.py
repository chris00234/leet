'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.

 

Example 1:

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.
Example 2:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 3:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= num <= 3999

'''

class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        divider = 1000
        while divider != 0:
            n = num // divider
            num = num - n*divider
            if n >= 0 and n <= 9:
                if divider == 1000:
                    result += n*'M'
                elif divider == 100:
                    if n == 4:
                        result += 'CD'
                    elif n == 9:
                        result += 'CM'
                    elif n == 5:
                        result += 'D'
                    else:
                        if n > 5:
                            result += 'D' + (n-5)*'C'
                        else:
                            result += n*'C'
                elif divider == 10:
                    if n == 4:
                        result += 'XL'
                    elif n == 9:
                        result += 'XC'
                    elif n == 5:
                        result += 'L'
                    else:
                        if n > 5:
                            result += 'L' + (n-5)*'X'
                        else:
                            result += n*'X'
                elif divider == 1:
                    if n == 4:
                        result += 'IV'
                    elif n == 9:
                        result += 'IX'
                    elif n == 5:
                        result += 'V'
                    else:
                        if n > 5:
                            result += 'V' + (n-5)*'I'
                        else:
                            result += n*'I'
                divider //= 10
        return result


if __name__ == '__main__':
    answer = Solution()
    print(answer.intToRoman(58))
    # print(4*'h')