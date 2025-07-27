def rabin_karp(text, pattern):

    match_found =[]

    n = len(text)

    m = len(pattern)    

    # Prime number to use for the hash function

    prime = 101   

    # Calculate the hash value of the pattern

    pattern_hash = 0

    for i in range(m):

        pattern_hash += ord(pattern[i])

    pattern_hash = pattern_hash % prime

    

    # Calculate the hash value of the first substring of the text

    text_hash = 0

    for i in range(m):

        text_hash += ord(text[i])

    text_hash = text_hash % prime

    # Iterate through the text, checking for matches with the pattern

    for i in range(n - m + 1):

        # Check if the current substring matches the pattern

        if text_hash == pattern_hash and text[i:i+m] == pattern:

            match_found.append(i)       

        # Calculate the hash value of the next substring

        if i < n - m:

            text_hash = (text_hash - ord(text[i]) + ord(text[i+m]))

            text_hash = text_hash % prime

    # No match found

    return match_found

text = 'abcdbabcdb'

pattern = 'abcdb'

print(rabin_karp(text, pattern))