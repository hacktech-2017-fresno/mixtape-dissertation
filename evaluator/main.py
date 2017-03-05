from language import get_annotated_text
from analysis import get_entity_score, get_sentiment_score

def evaluate_mixtape(text):
    doc = get_annotated_text(text)
    entity_score = get_entity_score(doc)
    sentiment_score = get_sentiment_score(doc)
    score = entity_score + sentiment_score
    return (entity_score, sentiment_score, score)