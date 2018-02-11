import logging

from data import *
from models.processors.text import TextProcessor
from .reports.context import ContextReport
from .reports.sentence import SentenceReport
from .reports.text import TextReport

logging.basicConfig(filename='analyzer.log',level=logging.DEBUG, filemode='w')


class Analyzer:

    @staticmethod
    def process_text(text):
        """ Process text. """
        logging.debug("Starting text processing...")
        output = TextReport(text=text)
        sentences = TextProcessor.get_sentences(text)
        for index, sentence in enumerate(sentences):
            report = Analyzer.process_sentence(sentence, index)
            if report:
                output.add(report)
        return output

    @staticmethod
    def process_sentence(sentence, index=None):
        """ Process sentence. """
        logging.debug("Starting sentence processing for '{0}'".format(sentence))
        output = SentenceReport(sentence=sentence, index=index)
        words = TextProcessor.get_words(Analyzer.__normalize_keywords(TextProcessor.normalize(sentence)))
        success = False
        for aspect_category in ASPECT_CATEGORIES:
            for keyword in ASPECT_CATEGORIES[aspect_category]:
                if Analyzer.__denormalize_key(keyword) in words:
                    logging.debug("Found keyword '{0}' in '{1}'".format(keyword, sentence))
                    reports = Analyzer.__process_context(words, Analyzer.__denormalize_key(keyword))
                    if reports:
                        success = True
                        logging.debug("Report created for '{0}'".format(sentence))
                        for report in reports:
                            report.category = aspect_category
                            output.add(report)
        output = output if success else None
        return output

    @staticmethod
    def __denormalize_key(word):
        return word.replace(' ', '_')

    @staticmethod
    def __normalize_key(word):
        return word.replace('_', ' ')

    @staticmethod
    def __normalize_keywords(text):
        for keyword in EVALUATION_VOCABULARY:
            if keyword in text:
                text = text.replace(keyword, Analyzer.__denormalize_key(keyword))

        for category in INTENSIFIER_VOCABULARY:
            for keyword in INTENSIFIER_VOCABULARY[category]:
                if keyword in text:
                    text = text.replace(keyword, Analyzer.__denormalize_key(keyword))

        for category in ASPECT_CATEGORIES:
            for keyword in ASPECT_CATEGORIES[category]:
                if keyword in text:
                    text = text.replace(keyword, Analyzer.__denormalize_key(keyword))

        return text

    @staticmethod
    def __process_context(sentence, word, index=None):
        logging.debug("Starting context processing for <{0}>".format(sentence))
        results = []
        index = TextProcessor.get_word_index(sentence, word) if not index else index
        lcontext = Analyzer.__get_left_context(sentence, index)
        rcontext = Analyzer.__get_right_context(sentence, index)
        for context in (lcontext, rcontext):
            evaluator, evaluation_rate = Analyzer.__get_evaluation(context)
            if evaluator:
                logging.debug("Evaluation word found: '{0}'".format(sentence))
                intensifier, intensifier_rate = Analyzer.__get_intensifier(context)
                inverter_word, success = Analyzer.__get_inverter(context)
                positive, negative = Analyzer.__get_keyword_summary(
                    rate=evaluation_rate,
                    multiplayer=intensifier_rate,
                    inverted=success
                )
                results.append(ContextReport(
                    keyword=Analyzer.__normalize_key(word),
                    evaluator=evaluator,
                    positive=positive,
                    negative=negative,
                    inverted=success,
                    intensifier=intensifier
                ))
        return results

    @staticmethod
    def __get_left_context(sentence, index):
        start = index - 3 if index - 3 > 0 else 0
        return sentence[start:index]

    @staticmethod
    def __get_right_context(sentence, index):
        end = index + 5 if index + 5 < len(sentence) else None
        return sentence[index + 1:end]

    @staticmethod
    def __get_evaluation(context):
        for context_word in context:
            if Analyzer.__normalize_key(context_word) in EVALUATION_VOCABULARY:
                return Analyzer.__normalize_key(context_word), \
                       EVALUATION_VOCABULARY[Analyzer.__normalize_key(context_word)]
        return None, None

    @staticmethod
    def __get_intensifier(context):
        for context_word in context:
            for intensifier_category in INTENSIFIER_VOCABULARY:
                if Analyzer.__normalize_key(context_word) in INTENSIFIER_VOCABULARY[intensifier_category]:
                    return Analyzer.__normalize_key(context_word), INTENSIFIER_RATES[intensifier_category]
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
