class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        while len(students):
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
            else:
                if sandwiches[0] not in students:
                    return len(students)
                students.append(students.pop(0))
        return 0
            
