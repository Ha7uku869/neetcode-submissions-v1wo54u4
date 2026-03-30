class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_char = ""
        for character in strs:
            encoded_char += str(len(character)) + '#' + character
        return encoded_char

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])

            word = s[j + 1: j + 1 + length]
            ans.append(word)

            i = j + 1 + length
        return ans
