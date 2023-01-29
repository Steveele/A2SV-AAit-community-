class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        result,left,right=0,0,0
        vowels='aeiou'
        vowel_counter=0

       for right in range(len(s)):

        
            if s[right] in vowels:
                vowel_counter+=1
            if (right-left + 1) == k:  
                result = max(result, vowel_counter)
                if s[left] in vowels: 
                    vowel_counter-=1
                left+=1
				
        return result

            
