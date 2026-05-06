class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        line = len(students)
        counter = Counter(students)

        for sandwich in sandwiches:
            if counter[sandwich] > 0:
                line -= 1
                counter[sandwich] -= 1
            else:
                break
        return line

        