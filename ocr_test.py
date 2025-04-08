import nltk 

with open('spanish_wordbank.txt', 'r') as file_in:
    spanish_wordbank = file_in.read().splitlines()

with open('corpus/rosa-fractales-czur-spa.txt', 'r') as file_in:
    raw_text = file_in.read()
raw_tokens = nltk.word_tokenize(raw_text)

lower_tokens = [word.lower() for word in raw_tokens]

# for word in lower_tokens:
#     if word not in spanish_wordbank:
#         print(word)

our_text = nltk.text.Text(lower_tokens)
print(our_text)