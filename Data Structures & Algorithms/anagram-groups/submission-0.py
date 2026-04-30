class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_list = {}
        anagram = []
        for word in strs:
            letter_list = sorted(word)
            signature_key = "".join(letter for letter in letter_list)
            if signature_key in set_list:
                set_list[signature_key].append(word)
            else:
                set_list[signature_key] = []
                set_list[signature_key].append(word)

        for key in set_list:
            anagram.append(set_list[key])
        return anagram