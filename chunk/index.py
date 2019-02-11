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
