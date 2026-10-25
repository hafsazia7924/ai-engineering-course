print("**Word Frequency Counter**")
sentence = input("Enter a sentence: ")

sentence = sentence.lower()
words = sentence.split()
#frequency dictionary is used to count words
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print(frequency)