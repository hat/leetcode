# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Note:

#     All inputs will be in lowercase.
#     The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        all_groups = []
        groups = {}
        # create dictionary to store letters sorted and index is already in dict
        # write to array
        for word in strs:
            if ''.join(sorted(word)) in groups:
                groups[''.join(sorted(word))].append(word)
            else:
                groups[''.join(sorted(word))] = [word]
        for group in groups:
            all_groups.append(sorted(groups[group]))
        return(all_groups)

answer = Solution()
print(answer.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))