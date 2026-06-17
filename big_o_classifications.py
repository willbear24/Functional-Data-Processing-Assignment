# Function A: This is an O(1) or constant time classification. It is completing one operation, returning the 0 index, so it would run the same regardless of the data set.
# Function B: This is an O(n) or linear time classification. It takes one pass through the list, adding items to the count if they equal the given target value.
# Function C: This is an O(n^2) or quadratic time classification. It contains and outer loop and an inner loop, so there are many many comparisons being done, which would exponentially increase the time it would take given the data set size. 
# Function D: This is an O(log n) or logorithmic time classification. N is cut roughly in half every time the loop iterates.
# Function E: This is an O(log n). While the sum and first parts of the function are liner and constant respectively, sorting data is a logorithmic function so it is the dominant time classification.

import time
import random

def count_pairs_quadratic(nums, target):
	"""O(n^2): check every unique pair with nested loops."""
	count = 0
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				count += 1
	return count


def count_pairs_linear(nums, target):
	"""O(n): count pairs using a frequency dictionary."""
	seen = {}
	count = 0

	for num in nums:
		complement = target - num
		count += seen.get(complement, 0)
		seen[num] = seen.get(num, 0) + 1

	return count

def benchmark(func, data, target):
    start = time.time()
    func(data, target)
    end = time.time()
    return end - start

sizes = [1000, 5000, 10000]

for size in sizes:
    data = list(range(size))
    random.shuffle(data)
	# Use a target that will usually produce no pairs, so both functions do comparable work.
    target = size * 2
	
    t1 = benchmark(count_pairs_quadratic, data, target)
    t2 = benchmark(count_pairs_linear, data, target)
	
    print(f"n={size:>6}   |   Quadratic: {t1:.4f}s   |   Linear: {t2:.4f}s")
	

# Benchmark output
# n=  1000   |   Quadratic: 0.0108s   |   Linear: 0.0001s
# n=  5000   |   Quadratic: 0.2447s   |   Linear: 0.0003s
# n= 10000   |   Quadratic: 0.9746s   |   Linear: 0.0006s
