import unittest

from models.analyzer import Analyzer
from models.loaders.template_loader import TemplateLoader
from models.processors.text import TextProcessor
from models.reports.context import ContextReport


class AnalyzerTest(unittest.TestCase):

    def setUp(self):
        self.input_text = "They underestimated the time some technical aspects took, but this didn't " \
                          "impact the overall creative timeline.  They delivered a lot of work that’s " \
                          "probably worth more than the scope. It was very whimsical and " \
                          "brand-appropriate and worked very well."

        self.sentence = "They underestimated the time some technical aspects took, " \
                        "but this didn't impact the overall creative timeline"

        self.words = [
            "They", "underestimated", "the", "time", "some", "technical", "aspects", "took,",
            "but", "this", "didn't", "impact", "the", "overall", "creative", "timeline"
        ]

        self.sentence_context_index = 3

        self.sentence_context = [
            "They", "underestimated", "the"
        ]

        self.evaluation = (None, None)

        self.intensifier = (None, None)

        self.inverter = (None, False)

        self.keyword_summary_test_data = {
            (0, 0): [0, ],
            (5, 0): [2.5, 2, False],
            (0, -3): [1, 3, True],
        }

        self.context_result = None

        self.sentence_result = [
            ContextReport(
                keyword="timeline",
                positive=2,
                negative=0
            )
        ]

    def test_get_context(self):
        result = Analyzer._Analyzer__get_context(self.words, self.sentence_context_index)
        self.assertListEqual(result, self.sentence_context)

    def test_get_evaluation(self):
        result = Analyzer._Analyzer__get_evaluation(self.sentence_context)
        self.assertEqual(result, self.evaluation)

    def test_get_intensifier(self):
        result = Analyzer._Analyzer__get_intensifier(self.sentence_context)
        self.assertEqual(result, self.evaluation)

    def test_get_inverter(self):
        result = Analyzer._Analyzer__get_inverter(self.sentence_context)
        self.assertEqual(result, self.inverter)

    def test_get_keyword_summary(self):
        for test_data in self.keyword_summary_test_data:
            result = Analyzer._Analyzer__get_keyword_summary(*self.keyword_summary_test_data[test_data])
            self.assertEqual(test_data, result)

    def test_process_context(self):
        result = Analyzer._Analyzer__process_context(self.words, self.words[self.sentence_context_index])
        self.assertEqual(result, self.context_result)

    def test_process_sentence(self):
        result = Analyzer.process_sentence(self.sentence).reports
        self.assertEqual(len(result), len(self.sentence_result))
        for expected, real in zip(result, self.sentence_result):
            self.assertEqual(expected.content, real.content)
            self.assertEqual(expected.positive, real.positive)
            self.assertEqual(expected.negative, real.negative)


class TextProcessorTest(unittest.TestCase):

    def setUp(self):
        self.input_text = "They underestimated the time some technical aspects took, but this didn't " \
                          "impact the overall creative timeline.  They delivered a lot of work that’s " \
                          "probably worth more than the scope. It was very whimsical and " \
                          "brand-appropriate and worked very well."

        self.normalized_text = "they underestimated the time some technical aspects took but this didn't " \
                               "impact the overall creative timeline. they delivered a lot of work that’s " \
                               "probably worth more than the scope. it was very whimsical and " \
                               "brand-appropriate and worked very well."

        self.sentences = [
            "They underestimated the time some technical aspects took, but this didn't impact the overall creative timeline.",
            "They delivered a lot of work that’s probably worth more than the scope.",
            "It was very whimsical and brand-appropriate and worked very well."
        ]

        self.sentence = "They underestimated the time some technical aspects took, " \
                        "but this didn't impact the overall creative timeline"

        self.words = [
            "They", "underestimated", "the", "time", "some", "technical", "aspects", "took,",
            "but", "this", "didn't", "impact", "the", "overall", "creative", "timeline"
        ]

    def test_normalize(self):
        result = TextProcessor.normalize(self.input_text)
        self.assertEqual(result, self.normalized_text)

    def test_get_sentences(self):
        result = TextProcessor.get_sentences(self.input_text)
        self.assertListEqual(result, self.sentences)

    def test_get_words(self):
        result = TextProcessor.get_words(self.sentence)
        self.assertListEqual(result, self.words)


class TemplateLoaderTest(unittest.TestCase):

    def setUp(self):
        template_dir = ""

    def test_load(self):
        TemplateLoader.load('text_report.txt')