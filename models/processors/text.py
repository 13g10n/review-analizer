import logging

logging.basicConfig(filename='analyzer.log',level=logging.DEBUG, filemode='w')


class TextProcessor:
    """Utility class for text-based operations, e.g. normalizing.
    """

    @staticmethod
    def normalize(text):
        """ Removes all punctuation marks from given text. """
        text = text.lower()
        text = text.replace(",", " ")
        text = text.replace(":", " ")
        text = text.replace(" -", " ")
        text = text.replace("- ", " ")
        while "  " in text:
            text = text.replace("  ", " ")
        return text

    @staticmethod
    def get_sentences(text):
        """ Returns list of sentences from given text. """
        result, sentence = [], ""
        delimiters = ('.', '!', '?')
        for index, letter in enumerate(text):
            sentence += letter
            if index == len(text) - 1:
                result.append(sentence.strip())
            elif letter in delimiters and TextProcessor.__get_next_letter(text, index) not in delimiters:
                result.append(sentence.strip())
                sentence = ""
        return result

    @staticmethod
    def get_words(sentence):
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
    def get_word_index(sentence, word):
        for index, item in enumerate(sentence):
            if word in item:
                return index
        return None

    @staticmethod
    def __get_next_letter(text, index):
        if index + 1 >= len(text):
            return None
        return text[index + 1]