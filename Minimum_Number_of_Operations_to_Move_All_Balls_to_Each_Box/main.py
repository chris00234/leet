class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ret = []
        i = 0

        for box in boxes:
            count = 0
            for tmp in range(i):
                if boxes[tmp] == '1':
                    count += i - tmp
                    
            for after in range(i + 1, len(boxes)):
                if boxes[after] == '1':
                    count += after - i
            ret.append(count)
            i += 1
        return ret
