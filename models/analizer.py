import logging

from data import *
from models.processors.text import TextProcessor
from .reports.context import ContextReport
from .reports.sentence import SentenceReport
from .reports.text import TextReport

logging.basicConfig(filename='analizer.log',level=logging.DEBUG, filemode='w')


class Analizer:

    @staticmethod
    def process_text(text):
        """ Process text. """
        logging.debug("Starting text processing...")
        output = TextReport(text=text)
        sentences = TextProcessor.get_sentences(text)
        for index, sentence in enumerate(sentences):
            report = Analizer.process_sentence(sentence, index)
            if report:
                output.add(report)
        return output

    @staticmethod
    def process_sentence(sentence, index=None):
        """ Process sentence. """
        logging.debug("Starting sentence processing for '{0}'".format(sentence))
        output = SentenceReport(sentence=sentence, index=index)
        words = TextProcessor.get_words(TextProcessor.normalize(sentence))
        success = False
        for aspect_category in ASPECT_CATEGORIES:
            for keyword in ASPECT_CATEGORIES[aspect_category]:
                if keyword in sentence:
                    logging.debug("Found keyword '{0}' in '{1}'".format(keyword, sentence))
                    report = Analizer.__process_context(words, keyword)
                    if report:
                        success = True
                        logging.debug("Report created for '{0}'".format(sentence))
                        report.category = aspect_category
                        output.add(report)
        output = output if success else None
        return output

    @staticmethod
    def __process_context(sentence, word, index=None):
        logging.debug("Starting context processing for <{0}>".format(sentence))
        index = TextProcessor.get_word_index(sentence, word.split()[0]) if not index else index
        context = Analizer.__get_context(sentence, index)
        evaluator, evaluation_rate = Analizer.__get_evaluation(context)
        if evaluator:
            logging.debug("Evaluation word found: '{0}'".format(sentence))
            intensifier, intensifier_rate = Analizer.__get_intensifier(context)
            inverter_word, success = Analizer.__get_inverter(context)
            positive, negative = Analizer.__get_keyword_summary(
                rate=evaluation_rate,
                multiplayer=intensifier_rate,
                inverted=success
            )
            return ContextReport(
                keyword=word,
                evaluator=evaluator,
                positive=positive,
                negative=negative,
                inverted=success,
                intensifier=intensifier
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
        multiplayer = 1 if not multiplayer else multiplayer
        result = (rate * multiplayer * -1) if inverted else (rate * multiplayer)
        return (result, 0) if result > 0 else (0, result)
