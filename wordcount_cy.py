import fileinput
import string
from collections import Counter
import csv
import json
import pickle


def to_word(words):
    line_words = []
    for word in words:
        if word:
            word = word.strip(string.punctuation)
            if word:
                line_words.append(word)
    return line_words


def main():
    all_words = []
    for line in fileinput.input():
        line_words = to_word(line.strip().split(' '))
        all_words.extend(line_words)

     
    counter = Counter(all_words)

    with open('wordcount.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['word', 'count'])
        for counting in counter.most_common():
            writer.writerow(counting)
    
    json.dump(counter.most_common(), open('wordcount.json', 'w'))
    
    pickle.dump(counter, open('wordcount.pkl', 'wb'))



if __name__ == '__main__':
    main()


