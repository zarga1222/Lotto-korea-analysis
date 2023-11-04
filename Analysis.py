import json
from collections import Counter

# Load JSON file
with open('lottor.json') as f:
    data = json.load(f)

# Flatten the list of lottery numbers
flat_list = [num for sublist in data for num in sublist]

# Calculate the frequency of each number
frequency = Counter(flat_list)

# Sort the frequencies in descending order and print the top 6 numbers
sorted_frequencies = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
top_6_numbers = [num for num, freq in sorted_frequencies[:6]]

print("Best next numbers:", top_6_numbers)
