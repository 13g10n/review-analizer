import logging

from data import *
from .reports.keyword import KeywordReport


logging.basicConfig(filename='analizer.log',level=logging.DEBUG, filemode='w')

class Analizer:
    @staticmethod
    def process_text(text):
        """ Process text. """
        logging.debug("Starting text processing...")
        normalized_text = Analizer.__normalize_text(text)
        sentences = Analizer.__get_sentences(normalized_text)
        positive, negative = 0, 0
        for index, sentence in enumerate(sentences):
            result = Analizer.process_sentence(sentence)
            for item in result:
                positive += item.positive
                negative += item.negative
                print("Sentence #{0}\n{1}".format(index+1, item))
        print("\n\nTotal: \t+{0} / -{1}".format(positive, negative))

    @staticmethod
    def process_sentence(sentence):
        """ Process sentence. """
        logging.debug("Starting sentence processing for '{0}'".format(sentence))
        results = []
        words = Analizer.__get_words(sentence)
        for aspect_category in ASPECT_CATEGORIES:
            for keyword in ASPECT_CATEGORIES[aspect_category]:
                if keyword in sentence:
                    logging.debug("Found keyword '{0}' in '{1}'".format(keyword, sentence))
                    report = Analizer.__process_context(words, keyword.split()[0])
                    if report:
                        logging.debug("Report created for '{0}'".format(sentence))
                        report.category = aspect_category
                        results.append(report)
        return results

    @staticmethod
    def __normalize_text(text):
        """ Removes all punctuation marks from given text. """
        text = text.lower()
        text = text.replace(",", " ")
        text = text.replace(":", " ")
        text = text.replace("-", " ")
        while "  " in text:
            text = text.replace("  ", " ")
        return text

    @staticmethod
    def __get_sentences(text):
        """ Returns list of sentences from given text. """
        return text.split(".")

    @staticmethod
    def __get_words(sentence):
        """ Returns list of words from given sentence. """
        logging.debug("Getting words for '{0}'".format(sentence))
        words = sentence.split()
        for index, _ in enumerate(words):
            words[index] = words[index].replace('!', '')
            words[index] = words[index].replace('?', '')
            words[index] = words[index].replace('.', '')
        logging.debug("Words returned: {0}".format(words))
        return words

    @staticmethod
    def __process_context(sentence, word, index=None):
        logging.debug("Starting context processing for <{0}>".format(sentence))
        index = sentence.index(word) if not index else index
        context = Analizer.__get_context(sentence, index)
        evaluation, evaluation_rate = Analizer.__get_evaluation(context)
        if evaluation:
            logging.debug("Evaluation word found: '{0}'".format(sentence))
            intensifier, intensifier_rate = Analizer.__get_intensifier(context)
            inverter_word, success = Analizer.__get_inverter(context)
            positive, negative = Analizer.__get_keyword_summary(
                rate=evaluation_rate,
                multiplayer=intensifier_rate,
                inverted=success
            )
            return KeywordReport(
                keyword=word,
                positive=positive,
                negative=negative
            )
        else:
            return None

    @staticmethod
    def __get_context(sentence, index):
        start = index - 3 if index - 3 > 0 else 0
        return sentence[start:index]

    @staticmethod
    def __get_evaluation(context):
        for context_word in context:
            if context_word in EVALUATION_VOCABULARY:
                return context_word, EVALUATION_VOCABULARY[context_word]
        return None, None

    @staticmethod
    def __get_intensifier(context):
        for context_word in context:
            for intensifier_category in INTENSIFIER_VOCABULARY:
                if context_word in INTENSIFIER_VOCABULARY[intensifier_category]:
                    return context_word, INTENSIFIER_RATES[intensifier_category]
        return None, None

    @staticmethod
    def __get_inverter(context):
        for context_word in context:
            if context_word in INVERTER_VOCABULARY:
                return context_word, True
        return None, False

    @staticmethod
    def __get_keyword_summary(rate=0, multiplayer=1, inverted=False):
        multiplayer = 1 if not multiplayer else 1
        rate = (rate * multiplayer * -1) if inverted else (rate * multiplayer)
        return (rate, 0) if rate > 0 else (0, rate)