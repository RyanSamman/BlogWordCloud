import re # Regular Expressions Library
import json
from collections import Counter

# Retrieve data
with open("processedData.json", "r") as file: 
    data = json.load(file) 

# Concatenate all blogs into one string
textData = " ".join(data)

# Remove newlines
textData = textData.replace("\n", " ")

# Get individual words
words = re.findall("[a-z\\']+", textData, flags=re.IGNORECASE)
print(words)

# Convert all words into lowercase
words = [w.lower() for w in words]
print(words)

# Count the word's appearences
sortedWords = dict(Counter(words).most_common(1000)) 

# Save Data
with open('processedData.json', "w") as file:
    json.dump(sortedWords, file, indent=2)