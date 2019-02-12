'''
Given an array and chunk size, divide the array into many subarrays
where each subarray is of length size
--- Examples
    chunk([1, 2, 3, 4], 2) --> [[ 1, 2], [3, 4]]
    chunk([1, 2, 3, 4, 5], 2) --> [[ 1, 2], [3, 4], [5]]
    chunk([1, 2, 3, 4, 5, 6, 7, 8], 3) --> [[ 1, 2, 3], [4, 5, 6], [7, 8]]
    chunk([1, 2, 3, 4, 5], 4) --> [[ 1, 2, 3, 4], [5]]
    chunk([1, 2, 3, 4, 5], 10) --> [[ 1, 2, 3, 4, 5]]
'''


# def chunk(array, size):
#     if len(array) < size or len(array) == 0 or size <= 0:
#         return array
#     chunked = []
#     for i in array:
#         if len(chunked) == 0 or len(chunked[-1]) == size:
#             chunked.append([i])
#         else:
#             chunked[-1].append(i)
#     return chunked


def chunk(array: list, size: int) -> list:
    if len(array) < size or len(array) == 0 or size <= 0:
        return array

    chunked = []
    index = 0
    while index < len(array):
        chunked.append(array[index:index + size])
        index += size
    return chunked
