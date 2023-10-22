def compress_string(s):
    if not s:
        return s 
      # If the string is empty, return it as it it
    compressed = []  
    count = 1  

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  # Increment the count for consecutive characters
        else:
            if count > 1:
                compressed.append(f"({count}, {s[i - 1]})")  # Append the compressed format
            else:
                compressed.append(s[i - 1])  # Append the character as it is
            count = 1  # Reset the count for the new character

    # Handle the last character
    if count > 1:
        compressed.append(f"({count}, {s[-1]})")
    else:
        compressed.append(s[-1])

    return ''.join(compressed)

# Input string
input_string = input("Enter the string to compress: ")

# Compress the string and print the result
compressed_string = compress_string(input_string)
print("Compressed String:", compressed_string)
