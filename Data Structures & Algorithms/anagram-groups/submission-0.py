class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)

        for word in strs:
            sorted_word = ''.join(sorted(word))
            str_dict[sorted_word].append(word)

        return list(str_dict.values())
