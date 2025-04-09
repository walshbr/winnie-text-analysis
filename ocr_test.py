import nltk 
from tqdm import tqdm
import time

# with open('spanish_wordbank.txt', 'r') as file_in:
#     spanish_wordbank = file_in.read().splitlines()

spanish_wordbank = nltk.corpus.cess_esp.words()


with open('corpus/rosa-fractales-czur-spa.txt', 'r') as file_in:
    raw_text = file_in.read()
raw_tokens = nltk.word_tokenize(raw_text)

lower_tokens = [word.lower() for word in raw_tokens]

# make it a set because jesus this was going to take 15 hours
lower_tokens = list(set(lower_tokens))
ocr_errors = []
max_num = len(lower_tokens)
with tqdm(total=max_num) as pbar:
    for word in lower_tokens:
        if word not in spanish_wordbank:
            ocr_errors.append(word)
        pbar.update(1)
    

# ocr_errors = [word for word in lower_tokens if word not in spanish_wordbank]

with open('errors.txt', 'w') as file_out:
    file_out.write(ocr_errors)

# for word in lower_tokens:
#     if word not in spanish_wordbank:
#         print(word)




# our_text = nltk.text.Text(lower_tokens)
# print(our_text)