'''Searching Challenge
Have the function SearchingChallenge(str) take the str parameter being passed and find the longest palindromic substring, which means the longest substring which is read the same forwards as it is backwards. For example: if str is "abracecars" then your program should return the string racecar because it is the longest palindrome within the input string.

The input will only contain lowercase alphabetic characters. The longest palindromic substring will always be unique, but if there is none that is longer than 2 characters, return the string none.
Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every fourth character with an underscore.

Your ChallengeToken: 6u4q1opf3a9
Examples
Input: "hellosannasmith"
Output: sannas
Final Output: san_as6_4q1_pf3_9
Input: "abcdefgg"
Output: none
Final Output: non_6u4_1op_3a9
'''

def longestPalindromicSubstring(s):
    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Find the longest palindromic substring of even size
        even_palindrome = expandAroundCenter(s, i, i + 1)
        if len(even_palindrome) > len(longest):
            longest = even_palindrome

        # Find the longest palindromic substring of odd size
        odd_palindrome = expandAroundCenter(s, i, i)
        if len(odd_palindrome) > len(longest):
            longest = odd_palindrome

    return longest if len(longest) > 2 else "none"

# Test cases
print(longestPalindromicSubstring("hellosannasmith"))  # Output: sannas
print(longestPalindromicSubstring("abcdefgg"))  # Output: none
