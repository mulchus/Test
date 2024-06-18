import numpy as np

# counts of each letter
sentence = "your sentence goes here"
print(list(sentence))
unique, counts = np.unique(list(sentence), return_counts=True)
print(unique, counts)
print(type(unique), type(counts))
print(dict(zip(unique, counts)))

