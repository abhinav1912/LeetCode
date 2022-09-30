class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
		#some var 
        result, break_loop, word = "", False, 0
		#looping for every letter(character)
        for letter in range(len(strs[0])):
		#looping for every word in the list
            for word in range(len(strs)-1):
				#the condition to stop searching
                try:
                    if strs[word][letter] != strs[word+1][letter]:
                        break_loop = True
                        break
                except IndexError:
                    break_loop = True
                    break
            if break_loop:
                break
			#save the character 
            result += strs[word][letter]
        return result
