from collections import defaultdict
from heapq import heappush, heappop

def huffman_encoding(text):
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

    return dict(sorted(heap[0][1:], key=lambda p: (len(p[-1]), p)))

def huffman_decoding(encoded_text, code_table):
    decoded_text = ""
    i = 0
    while i < len(encoded_text):
        for symbol, code in code_table.items():
            if encoded_text.startswith(code, i):
                decoded_text += symbol
                i += len(code)
                break
    return decoded_text
#####################################################################
text1 = "abcdefgg"

frequency1 = defaultdict(int)
for character in text1:
    frequency1[character] += 1

code_table1 = huffman_encoding(text1)

encoded_text1 = ""
for character in text1:
    encoded_text1 += code_table1[character]

decoded_text1 = huffman_decoding(encoded_text1, code_table1)

print("Exemplo 1")
print("Texto original:", text1)
print("Tabela de codificação:", code_table1)
print("Texto codificado:", encoded_text1)
print("Texto decodificado:", decoded_text1)
print()
####################################################################
text2 = "abcdefggb"

frequency2 = defaultdict(int)
for character in text2:
    frequency2[character] += 1

code_table2 = huffman_encoding(text2)

encoded_text2 = ""
for character in text2:
    encoded_text2 += code_table2[character]

decoded_text2 = huffman_decoding(encoded_text2, code_table2)

print("Exemplo 2")
print("Texto original:", text2)
print("Tabela de codificação:", code_table2)
print("Texto codificado:", encoded_text2)
print("Texto decodificado:", decoded_text2)
print()
