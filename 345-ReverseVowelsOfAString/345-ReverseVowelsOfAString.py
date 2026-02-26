# Last updated: 2/26/2026, 1:36:28 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0, len(s)-1
        word = list(s)
        vowels = set("aeiou")
        while l<r:
            if word[l].lower() in vowels and word[r].lower() in vowels:
                temp = word[l]
                word[l] = word[r]
                word[r] = temp
                l+=1
                r-=1
            elif word[l].lower() not in vowels:
                l+=1
            else:
                r-=1
        return ''.join(word)


        