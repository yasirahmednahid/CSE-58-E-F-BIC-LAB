text = input()
k = int(input())

freq = {}
for i in range(len(text) - k + 1):
    pattern = text[i:i+k]
    freq[pattern] = freq.get(pattern, 0) + 1

max_count = max(freq.values())
for pattern, count in freq.items():
    if count == max_count:
        print(pattern,end= "")
