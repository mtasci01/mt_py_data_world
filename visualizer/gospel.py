import json
import requests
from matplotlib import pyplot as plt

# visualizing word frequencies in the gospels

MAX_COUNT_RESULTS = 50
HORIZONTAL_CHART = True

response = requests.get('http://localhost:8000/gospel_analysis', json=[])
resp_json = json.loads(response.text)
word_counts = resp_json['word_counts']
print("word_counts received: " + str(len(word_counts)))

tokens = []
counts = []
for i in range(len(word_counts)):
    if i > MAX_COUNT_RESULTS:
        break
    tokens.append(word_counts[i]['token'])
    counts.append(word_counts[i]['cnt'])

if not(HORIZONTAL_CHART):
    plt.xticks(rotation='vertical')
    plt.bar(tokens, counts)
    plt.xlabel('Token')
    plt.ylabel('Frequency')
else:
    tokens.reverse()
    counts.reverse()
    plt.barh(tokens, counts) 
    plt.xlabel('Frequency')
    plt.ylabel('Token')
plt.title('Gospel Word Frequency')    
plt.show()       
        
