import unittest
from language import get_annotated_text
from analysis import get_entity_score, get_sentiment_score

class TestScoreAnalysis(unittest.TestCase):

    def test_entity_score(self):
        text = "You ask, what is our aim? I can answer in one word. It is victory. Victory at all costs - Victory in spite of all terrors - Victory, however long and hard the road may be, for without victory there is no survival. Let that be realized. No survival for the British Empire, no survival for all that the British Empire has stood for, no survival for the urge, the impulse of the ages, that mankind shall move forward toward his goal."
        doc = get_annotated_text(text)
        entity_score = get_entity_score(doc)
        self.assertLessEqual(entity_score,10)

    def test_sentiment_score(self):
        text = "You ask, what is our aim? I can answer in one word. It is victory. Victory at all costs - Victory in spite of all terrors - Victory, however long and hard the road may be, for without victory there is no survival. Let that be realized. No survival for the British Empire, no survival for all that the British Empire has stood for, no survival for the urge, the impulse of the ages, that mankind shall move forward toward his goal."
        doc = get_annotated_text(text)
        sentiment_score = get_sentiment_score(doc)
        self.assertIsInstance(sentiment_score, float)

if __name__ == '__main__':
    unittest.main()