def find_increasing_subsequences(s):
    steps = 0
    n = len(s)

    # dp[i] represents a list of increasing subsequences ending at index i
    dp = [[] for _ in range(n)]

    # Initialize each element in dp with a list containing the single character
    for i in range(n):
        dp[i].append([s[i]])

    # Iterate through the string to find the increasing subsequences
    for i in range(1, n):
        for j in range(0, i):
            if s[i] > s[j]:
                for subseq in dp[j]:
                    steps = steps+1
                    print(steps)
                    dp[i].append(subseq + [s[i]])
            else:
                steps = steps+1
                print(steps)                

    # Concatenate all the lists in dp to get the total list of increasing subsequences
    result = [subseq for sublist in dp for subseq in sublist]

    return result

# Example usage:
numeric_string = "1234"
result = find_increasing_subsequences(numeric_string)
print(f"The increasing subsequences in {numeric_string} are: {result}")
