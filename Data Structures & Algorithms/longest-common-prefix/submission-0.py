class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""

        for char in strs[0]:
            if all(string.startswith(common + char) for string in strs):
                common += char
            else:
                break

        return common