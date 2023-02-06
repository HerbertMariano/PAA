from collections import defaultdict
from heapq import heappush, heappop

def get_ternary_huffman_codes(text):
    frequency = defaultdict(int)
    for character in text:
        frequency[character] += 1

    heap = [[weight, [character, ""]] for character, weight in frequency.items()]
    heap = sorted(heap, reverse=True)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))


print(get_ternary_huffman_codes('abcdddddahud'))