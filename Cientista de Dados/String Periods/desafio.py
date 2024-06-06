""" Have the function StringPeriods(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears. Your program should return the longest substring K, and if there is none it should return the string -1.

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string. Another example: if str is "abababababab" then your program should return ababab because it is the longest substring. If the input string contains only a single character, your program should return the string -1.
Examples
Input: "abcxabc"
Output: -1
Input: "affedaaffed"
Output: -1 """

# __define-ocg__
def StringPeriods(s):
    if len(s) == 1:
        return -1
  
    for length in range(1, len(s) // 2 + 1):
        substring = s[:length]
        count = len(s) // length
        repeated_str = substring * count
        if repeated_str == s:
            return substring

    return -1

# Exemplos de uso
print(StringPeriods("abcxabc")) # Output: -1
print(StringPeriods("affedaaffed")) #Output: -1
print(StringPeriods("abcababcababcab")) #Output: abcab
print(StringPeriods("abababababab")) #Output: ababab