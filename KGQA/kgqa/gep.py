# import re

import pandas as pd
import spacy

from kgqa.processor import ComplexFunc
from kgqa.utils.utils import change_nouns


class GetEntity:

    def __init__(self):
        super(GetEntity, self).__init__()
        self.processor = ComplexFunc()
        self.nlp = spacy.load('en_core_web_sm')
        self.change = change_nouns()

    def preprocess_text(self, input_file):
        text_strip = [text.strip() for text in input_file]
        preprocessed_text = [text for text in text_strip if text not in ('', ' ')]
        text = " ".join(preprocessed_text)
        text = self.change.resolved(text)
        text = self.nlp(text)
        return text

    def get_entity(self, text):
        ent_pairs, final_entity_pairs = [],[]
        sentences = [one_sentence.text.strip() for one_sentence in text.sents]

        for one_sentence in sentences:
            final_entity_pairs = []
            one_sentence = self.nlp(one_sentence)

            dep = [token.dep_ for token in one_sentence]

            normal_sent_ = self.processor.normal_sent(one_sentence)

            if normal_sent_:
                for pair in normal_sent_:
                    ent_pairs.append(pair)

                pairs = pd.DataFrame(ent_pairs, columns=['source', 'relation', 'aux_relation', 'target', 'time', 'place'])
                number_of_ent_pairs = str(len(ent_pairs))

                final_entity_pairs.append(pairs)

        if final_entity_pairs:
            return final_entity_pairs, number_of_ent_pairs    
        return None, None
