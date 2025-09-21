# Solucion eficiente del problema 128 de leetcode
# O(n)
def longestConsecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:  # Solo empiezo desde inicios de secuencia
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)

    return longest
