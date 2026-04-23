class Solution:
    def calPoints(self, operations: List[str]) -> int:
        new_score = []
        pointer = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                two_sum = int(new_score[pointer-1]) + int(new_score[pointer-2])
                new_score.append(two_sum)
                pointer += 1
            elif operations[i] == "C":
                new_score.pop()
                pointer -= 1
            elif operations[i] == "D":
                new_score.append(2 * int(new_score[pointer - 1]))
                pointer += 1
            else:
                new_score.append(int(operations[i]))
                pointer += 1
        
        return sum(new_score)

        