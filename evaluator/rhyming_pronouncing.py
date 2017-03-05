import pronouncing


def getRhymes(word):
    """Get rhymes."""
    return pronouncing.rhymes(word)


def rhymeComparison(word1, word2):
    """Perfect rhyming."""
    set_rhyme = getRhymes(word1)
    print set_rhyme
    return word1 in set_rhyme


def test():
    """Testing Frames."""
    print rhymeComparison("hello", "mellow")


if __name__ == "__main__":
    test()
