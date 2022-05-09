class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])
        ans = list(mapping[digits[0]])
        for i in range(1, len(digits)):
            digit = digits[i]
            temp = []
            for j in ans:
                for k in mapping[digit]:
                    temp.append(j+k)
            ans = temp
        return temp
