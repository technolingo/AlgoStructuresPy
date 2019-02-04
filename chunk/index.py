# def chunk(array, size):
#     chunked = []
#     for i in array:
#         if len(chunked) == 0 or len(chunked[-1]) == size:
#             chunked.append([i])
#         else:
#             chunked[-1].append(i)
#     return chunked

def chunk(array: list, size: int) -> list:
    chunked = []
    index = 0;
    while index < len(array):
        chunked.append(array[index:index + size])
        index += size;
    return chunked

print(chunk([1,2,3,4,5,6,7,8,9,10], 3))
