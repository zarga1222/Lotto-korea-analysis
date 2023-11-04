import pandas as pd
from collections import Counter

def best_next_numbers(file_path):
    # Load CSV file using pandas
    data = pd.read_csv(file_path)

    # Flatten the list of lottery numbers
    flat_list = [num for sublist in data.values for num in sublist]

    # Calculate the frequency of each number
    freq = Counter(flat_list)

    # Sort the frequencies in descending order and select the top 6 numbers
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    best_numbers = [num for num, freq in sorted_freq[:6]]

    return best_numbers

file_path = 'your_file_path_here.csv'
print(best_next_numbers(file_path))
