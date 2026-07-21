class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        print("".join(res))
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        if len(s) != 0:
            length = s[0]
            tmp = ''.join(s.split(str(length)))
            return tmp.split('#')[1:]
        return []