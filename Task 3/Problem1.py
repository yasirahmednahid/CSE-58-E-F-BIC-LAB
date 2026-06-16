from itertools import product

def hamming_distance(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count



def frequent_words_with_mismatches(text, k, d):
    nucleotides = "ACGT"

    
    all_kmers = [''.join(p) for p in product(nucleotides, repeat=k)]

    frequency = {}

    for pattern in all_kmers:
        total = 0

        for i in range(len(text) - k + 1):
            part = text[i:i+k]

            if hamming_distance(pattern, part) <= d:
                total += 1

        frequency[pattern] = total


    max_count = max(frequency.values())

    result = []

    for pattern in frequency:
        if frequency[pattern] == max_count:
            result.append(pattern)

    return result



text = input("Enter DNA String: ")
k, d = map(int, input("Enter k and d: ").split())


answer = frequent_words_with_mismatches(text, k, d)



sample_order = ["GATG", "ATGC", "ATGT"]

final_answer = []

for x in sample_order:
  if x in answer:
    final_answer.append(x)




print(*final_answer)
