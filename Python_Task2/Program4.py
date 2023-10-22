# Initialize an empty list to store the numbers that meet the criteria
result = []

for num in range(2000, 3201):
    # Check if the number is divisible by 7 and not a multiple of 5
    if num % 7 == 0 and num % 5 != 0:
        result.append(str(num))  # Convert the number to a string and add it to the result list


result_sequence = ', '.join(result)

print(result_sequence)
