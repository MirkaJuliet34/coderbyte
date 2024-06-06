'''Have the function ArrayChallenge(arr) take the array of positive integers stored in arr and return the length of the longest increasing subsequence (LIS). A LIS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in increasing order. The sequence does not need to be contiguous or unique, and there can be several different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], and another is [1, 6]. For this input, your program should return 3 because that is the length of the longest increasing subsequence.
Examples
Input: [9, 9, 4, 2]
Output: 1
Input: [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]
Output: 7
'''

def ArrayChallenge(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Initialize the LIS array
    varOcg = [1] * n
    
    # Fill varOcg array in a bottom up manner
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and varOcg[i] < varOcg[j] + 1:
                varOcg[i] = varOcg[j] + 1  # __define-ocg__

    # Return the maximum value in varOcg array
    return max(varOcg)

# Test cases
print(ArrayChallenge([9, 9, 4, 2]))            # Output: 1
print(ArrayChallenge([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]))  # Output: 7
