from rhyming_api import matchingRhyme
import re

# Naive check for the last words matching, if they do.

def get_ending_words_from_sentences(sentences):
    word_list = []

    for sentence in sentences:
        match = re.search(r'\s(\w+)[\.!?]',sentence.content)
        word_list.append(match.group(0))

    return word_list

# Doesn't work at the moment. Oops.

def get_rhyming_score(sentences):
    word_list = get_ending_words_from_sentences(sentences)

    # Super naive.
    sum = 0
    for word in word_list:
        for other_word in word_list:
            if word != other_word:
                if matchingRhyme(word,other_word) :
                    sum += 10

    return sum