# The findRepeatedDnaSequences method finds all 10-letter sequences that appear more than once in `s`.

# Approach:
# - Use a hashmap to count occurrences of 10-character substrings.
# - If a substring appears twice, add it to the result.

# TC: O(n) - Single pass through `s`.
# SC: O(n) - Space for the hashmap.


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        map = {}
        result = []

        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            if substring in map:
                if map[substring] == 1:
                    result.append(substring)
                map[substring] += 1
            else:
                map[substring] = 1
        
        return result