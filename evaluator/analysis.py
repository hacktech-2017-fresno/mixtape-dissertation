# Entity Scores
# Rappers should reference significant things
# Because of that, we're going to grade based on that hip referencing!
entityTypes = {
    'CONSUMER_GOOD': 5,
    'EVENT': 2,
    'LOCATION': 2,
    'ORGANIZATION': 3,
    'OTHER': 1,
    'PERSON': 4,
    'UNKNOWN':  0,
    'WORK_OF_ART': 3
}

def get_entity_tuple(doc_entity):
    return (doc_entity.entity_type, doc_entity.salience)

def make_entity_tuple_list(doc):
    list = []
    for entity in doc.entities:
        list.append(get_entity_tuple(entity))
    return sorted(list, key=lambda (a,b): b)

def make_entity_pp_score(list):
    sum = 0
    distribution = 1 / len(list)
    counter = 0
    for s in list:
        sum += (entityTypes[s[0]]*s[1]) * (1 - counter*distribution)
        counter += 1
    return sum*10

def get_entity_score(doc):
    tuple_list = make_entity_tuple_list(doc)
    return make_entity_pp_score(tuple_list)

# Sentiment Scores
# Rappers should start from the bottom, now we here.
# Because of that, we're going to grade based on that raw, emotion, an.

def get_sentence_sentiment_tuple(doc_sentence):
    return (doc_sentence.sentiment.score, doc_sentence.sentiment.magnitude)

def make_sentence_sentiment_tuple_list(doc, sort_by_magnitude=True):
    list = []
    for sentence in doc.sentences:
        list.append(get_sentence_sentiment_tuple(sentence))
    sorted(list, key=lambda (a, b): b if sort_by_magnitude else a)
    return list

def make_sentiment_pp_score(list):
    sum = 0
    distribution = 1 / len(list)
    counter = 0
    for s in list:
        sum += (s[0]*s[1]) * (1 - counter*distribution)
        counter += 1
    return sum

def judge_sentiment_pp_score(pp_score):
    if pp_score > 1.0:
        return 20.0
    elif pp_score > 0.5:
        return 50.0*pp_score
    elif pp_score > 0:
        return 60.0*(1-pp_score)
    elif pp_score > -3.0:
        return 80.0*(-1*pp_score)
    else:
        return 80.0

def get_sentiment_score(doc):
    tuple_list = make_sentence_sentiment_tuple_list(doc)
    pp_score = make_sentiment_pp_score(tuple_list)
    return judge_sentiment_pp_score(pp_score)