class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(" ")
        

        for i, word in enumerate(sentence):
            l = 100000000
            for key in dictionary:
                if word.startswith(key):
                    if l > len(key):
                        sentence[i] = key
                        l = len(key)
                
                
        
        ret = ""

        for word in sentence:
            ret += word
            ret += " "
        ret = ret[:-1]
        return ret

