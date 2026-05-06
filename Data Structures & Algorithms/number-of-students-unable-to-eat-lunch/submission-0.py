class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        line = len(students)
        while line > 0 and sandwiches[0] in students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                print(students, sandwiches)
                line -= 1
            else:
                temp = students[0]
                for i in range(line - 1):
                    students[i] = students[i + 1]
                students[-1] = temp
                print(students, sandwiches)

        if students is None:
            return 0
        else:
            return len(students)
            
                
        
        # def movearr(self):        
        #     temp = students[-1]
        #     for i in range(line - 1):
        #         students[i] = students[i + 1]