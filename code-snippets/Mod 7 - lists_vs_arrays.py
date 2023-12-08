import time
import numpy as np

# Create a large dataset
large_dataset = list(range(10**6))  # 1 million elements

# Using Python List (for loop)
start_time = time.time()

squares_list = []
for num in large_dataset:
    squares_list.append(num ** 2)

end_time = time.time()
list_execution_time = end_time - start_time
print(f"Using Python List took {list_execution_time} seconds")

# Using NumPy Array (vectorized operation)
start_time = time.time()

np_large_dataset = np.array(large_dataset)
squares_array = np_large_dataset ** 2

end_time = time.time()
array_execution_time = end_time - start_time
print(f"Using NumPy Array took {array_execution_time} seconds")

# Calculate the performance improvement
performance_improvement = list_execution_time / array_execution_time
print(f"NumPy Array is {performance_improvement:.2f} times faster than Python List.")
