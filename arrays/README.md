# Arrays

- arrays often have brute force solutions using O(n) space
    - there are solutions that use the array itself to reduce space complexity to O(1)
- consider processing the digits from the back or reversing the array
- operate on subarrays
- do not worry about preserving integrity of the array (sortedness, equal entries together, etc) until it is time to return
- arrays are good data structure if distribution of elements are known in advance
    - using boolean array to represent subset of integers 1, ..., n
- use parallel logic on rows and columns for 2D arrays
- attempt to simulate the specifications than to analytically solve for the result
    - rather than writing a formula for the i-th entry in spiral order in n x n matrix, just compute output from beginning
