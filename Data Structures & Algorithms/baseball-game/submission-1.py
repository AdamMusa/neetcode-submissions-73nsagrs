class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            if operations[i] == "1":
                record.append(int(operations[i]))
            elif operations[i] == "2":
                record.append(int(operations[i]))
            elif operations[i] == "+":
                record.append(record[-1] + record[-2])
            elif operations[i] == "C":
                record.pop()
            elif operations[i] == "5":
                record.append(int(operations[i]))
            elif operations[i] == "D":
                record.append(record[-1]*2)
            else:
                record.append(operations[i])
        return sum(record)