import numpy as np

''' multidimensional arrays '''
# single dimension array
arr_s = np.arange(10)

# reshaping into 2 dimensions
arr_2d = arr_s.reshape(2, 5)

# creating a 2d dimensional
my_2d = np.array([[85, 90, 92],[88, 89, 91], [75, 78, 82], [93, 94, 96]])

# creating a 3 dimensional 
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])


''' advanced indexing '''
# Create a 2D array (matrix) 
scores = np.array([
    [85, 90, 92],
    [88, 89, 91],
    [75, 78, 82],
    [93, 94, 96]
])

my_list = [[85, 90, 92],
           [88, 89, 91],
           [75, 78, 82],
           [93, 94, 96]]

# basic indexing works for both


# advanced indexing only for arrays
print(my_list[1, 2]) # error

print(scores[1, :])

# Select the third column (index 2)
third_column = scores[:, 2]

# Select a subset of the matrix (rows 1 and 3, columns 0 and 2)
subset = scores[[1, 3], [0, 2]]
# rows 0:2, columns 1:3
subset = scores[0:2, 1:3]  

# assigning a value in a specific position row 0 column 3
scores[0, 2] = 20

# assigning zero to the last row
scores[-1, :] = 0


''' mathematical methods '''
scores.mean()
scores.sum()
scores.sum(axis=0)

# Select scores greater than 90
high_scores = scores[scores > 90]

# return boolean according to condition
scores == 90

# Select rows where the first column value is greater than 85
selected_rows = scores[scores[:, 0] > 85]

# swapping axis
print(scores.swapaxes(1,0))


''' numerical computations and vectorisation '''

ls = [1, 2, 3]

arr = np.array(ls)

# adding 4 to each element of list
ls = ls + 4
# error with lists	

# adding 4 to each element of Numpy array
arr = arr + 4

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 9, 8, 7, 6, 5]
list3 = []

# solutions with loop
for x, y in zip(list1, list2):
    list3.append(x * y)

# with numpy arrays
arr1 = np.array(list1)
arr2 = np.array(list2)

print(list1*list2)
