class Solution:

    def encode(self, strs: List[str]) -> str:
        op = ""
        for s in strs:
            op += str(len(s)) + "#" + s
        return op

    def decode(self, s: str) -> List[str]:
        op = []

        while s:
            index = s.find("#")
            num = int(s[:index])

            word = s[index + 1 : index + 1 + num]
            op.append(word)

            s = s[index + 1 + num :]

        return op