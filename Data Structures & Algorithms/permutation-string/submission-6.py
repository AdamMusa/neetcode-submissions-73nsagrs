class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for c in s1:
            count[c] = count.get(c, 0) +1
        need = len(count)
        for i in range(len(s2)):
            count1, curr = {}, 0
            for j in range(i, len(s2)):
                count1[s2[j]] = 1 + count1.get(s2[j], 0)
                if count.get(s2[j], 0) < count1[s2[j]]:
                    break
                if count.get(s2[j],0) == count1[s2[j]]:
                    curr +=1
                if need == curr:
                    return True
        return False