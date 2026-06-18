# Function A: This is an O(n) space complexity because it is returning a list the same size as the original, just reversed so it would need space proportional to the size of the original list.
def reverse_string(s):
    return s[::-1]

# Function B: This is also an O(n) space complexity because it is returning a dictionary of the counts of characters in a given text. The more text, the larger the count so it grows proportionally to the size of the data input. 
def count_letters(text):
    counts = {}
    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

# Function C: This is a O(n²) space complexity because it creates an n by n matrix, storing the whole matrix in memory. 
def matrix_identity(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

# Function D: This is a O(1) space complexity because regardless of the data set of numbers it is always producing a single output in the form of a running sum, taking up the same amount of memory every time. 
def running_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    print(total)

import csv

def duplicates_set(file_path='emails.csv', email_column='email'):
    """Find duplicate emails using a fast, memory-heavy set approach (O(n) time, O(n) space)."""
    seen = set()
    duplicates = set()

    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_email = row.get(email_column, '')
            email = raw_email.strip().lower()
            if not email:
                continue
            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)

    return duplicates

def duplicates_sort(file_path='emails.csv', email_column='email'):
    """Find duplicate emails using a slower, memory-saving approach O(n log n) time, O(n) space."""
    all_emails = []
    duplicates = set()

    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_email = row.get(email_column, '')
            email = raw_email.strip().lower()
            if not email:
                continue
            all_emails.append(email)

        all_emails.sort()

    for i in range(len(all_emails) - 1):
        if all_emails[i] == all_emails[i + 1]:
            duplicates.add(all_emails[i])

    return duplicates


