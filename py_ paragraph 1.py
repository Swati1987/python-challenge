import re
paragraph = ""

with open("pyparagraph.txt") as txt_data:
 paragraph = txt_data.read()

word_split = paragraph.split(" ")
word_count = len(word_split)

letter_counts = []

for word in word_split:

    letter_counts.append(len(word))

avg_letter_count = sum(letter_counts) / float(len(letter_counts))

sentence_split = re.split("(?<=[.!?]) +", paragraph)

print(sentence_split)
sentence_count = len(sentence_split)

words_per_sentence = []


for sentence in sentence_split:

    words_per_sentence.append(len(sentence.split(" ")))

avg_sentence_len = sum(words_per_sentence) / float(len(words_per_sentence))


print ("Paragraph Analysis")
print ("------------------")

print ("Approximate Word Count: " + str(word_count))
print ("Approximate Sentence Count: " + str(sentence_count))
print ("Average Letter Count: " + str(avg_letter_count))
print ("Average Sentence Length: " + str(avg_sentence_len))