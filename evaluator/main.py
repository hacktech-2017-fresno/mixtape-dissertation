from language import get_annotated_text
from analysis import get_entity_score, get_sentiment_score

def evaluate_mixtape(text):
    doc = get_annotated_text(text)
    score = get_entity_score(doc) + get_sentiment_score(doc)
    return score