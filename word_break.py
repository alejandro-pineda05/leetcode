from typing import List

# Problema 139 leetcode

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return wordBreak2(s, set(wordDict), set())



def wordBreak2(s, word_set, valores_falsos):
    if s in valores_falsos:
        print("entra")
        return False
    print(f"s: {s}")

    current_word = ""

    i = 0
    while i < len(s):
        current_word += s[i]
        i += 1

        print(current_word)


        if current_word in word_set:
            if i == len(s):
                return True

            elif wordBreak2(s[i:len(s)], word_set, valores_falsos) == True:
                return True
    
    valores_falsos.add(s)
    return False



# Tests

#print(wordBreak("leetcode", ["leet","code"]))

#print(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))

#print(wordBreak("catsandog", ["cats", "cat", "and", "sand", "dog"]))