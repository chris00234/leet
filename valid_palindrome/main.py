class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ""
        for letter in s:
            if 'Z' >= letter >= 'A' or 'a' <= letter <= 'z':
                sentence += letter.lower()
            if letter >= '0' and letter <= '9':
                sentence += letter
        
        reverse_sentence = ""

        for i in range(len(sentence) - 1, -1, -1):
            reverse_sentence += sentence[i]
        print(sentence)
        if reverse_sentence == sentence:
            return True
        return False