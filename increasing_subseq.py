def count_increasing_subsequences(s):
    n = len(s)
    
    # dp[i] represents the count of increasing subsequences ending at index i
    dp = [0] * n
    
    # Initialize each element in dp to 1 since a single character is an increasing subsequence.
    for i in range(n):
        dp[i] = 1
    
    # Iterate through the string to calculate the count of increasing subsequences.
    for i in range(1, n):
        for j in range(0, i):
            if s[i] > s[j]:
                dp[i] += dp[j]
    
    # Sum up all the counts in dp to get the total number of increasing subsequences.
    total_count = sum(dp)
    
    return total_count

# Example usage:
numeric_string = "1234"
result = count_increasing_subsequences(numeric_string)
print(f"The number of increasing subsequences in {numeric_string} is: {result}")

