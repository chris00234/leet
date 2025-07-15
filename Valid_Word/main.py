class Solution:
    def isValid(self, word: str) -> bool:
        numCharacter = 0
        numVowel = 0
        numConsonant = 0
        vowels = ['a','e','i','o','u']

        for char in word:
            if not char.isalnum():
                return False
            numCharacter += 1
            if char.lower() in vowels:
                numVowel += 1
            elif char.lower().isalpha():
                numConsonant += 1
        
        return True if numCharacter >= 3 and numVowel >= 1 and numConsonant >= 1 else False


