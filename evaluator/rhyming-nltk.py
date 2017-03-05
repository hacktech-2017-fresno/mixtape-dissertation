import nltk


"""
Pros and cons of this script:
    Pros: Unlimited
    Cons: Require to download the data set of nltk.corpus.cmudict
            and also slow.
"""


# Perfect Rhyme
def getRhyme(inp, level):
    """Get rhyme by using nltk cmudict"""
    entries = nltk.corpus.cmudict.entries()
    syllables = [(word, syl) for word, syl in entries if word == inp]
    rhymes = []
    for (word, syllable) in syllables:
        rhymes += [word for word, pron in entries if pron[-level:] ==
                   syllable[-level:]]
    return set(rhymes)


def rhymeComparison(word1, word2, level=1):
    """Compare words with perfect rhymes"""
    #   if word1.find ( word2 ) == len(word1) - len ( word2 ):
    #     return False
    # if word2.find ( word1 ) == len ( word2 ) - len ( word1 ):
    #     return False
    # print set_rhyme
    set_rhyme = getRhyme(word2, level)
    return word1 in set_rhyme


def test():
    """Test Module."""
    print rhymeComparison("Hello", "yellow")


if __name__ == "__main__":
    test()
