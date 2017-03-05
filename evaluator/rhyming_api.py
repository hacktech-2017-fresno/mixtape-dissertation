import requests


"""
Pros and cons of this script:
    Pros: Fast and Accessible
    Cons: Only 350 requests / hour
"""


def requestURL(word):
    """Returning Correct URL for request.

    Example URL:
        http://rhymebrain.com/talk?function=getRhymes&word=hello

    """
    url = url = "http://rhymebrain.com/talk?function=getRhymes&word="
    return url + word


def getResponse(url):
    """Get JSON Response from Requests."""
    response = requests.get(url)
    data = response.json()
    return data


def getRhymes(word):
    """Combination of requestURL and getResponse."""
    url = requestURL(word)
    data = getResponse(url)
    return data


def matchingRhyme(word1, word2):
    """Matching one rhyme to the other"""
    rhymes1 = getRhymes(word1)

    for entries in rhymes1:
        if entries['word'] == word2:
            if entries['score'] > 250:
                return True
            else:
                return False

    return False


def test():
    """Test Module."""
    print matchingRhyme("yellow", "mellow")


if __name__ == "__main__":
    test()
