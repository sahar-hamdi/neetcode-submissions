class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for stri in strs:
            encoded.append(f"{len(stri)}#{stri}")
        
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            lenn = int(s[i:j])

            word = s[j + 1 : j + 1 + lenn]
            res.append(word)

            i = j + 1 + lenn

        return res