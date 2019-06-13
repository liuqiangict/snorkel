import unittest
from types import SimpleNamespace

from snorkel.labeling.preprocess import PreprocessorMode
from snorkel.labeling.preprocess.nlp import SpacyPreprocessor

DATA = ["Jane", "Jane plays soccer."]


class TestSpacyPreprocessor(unittest.TestCase):
    def test_spacy_preprocessor(self) -> None:
        example = SimpleNamespace(text=DATA[1])
        preprocessor = SpacyPreprocessor("text", "doc")
        preprocessor.set_mode(PreprocessorMode.NAMESPACE)
        example_preprocessed = preprocessor(example)
        self.assertEqual(len(example_preprocessed.doc), 4)
        token = example_preprocessed.doc[0]
        self.assertEqual(token.text, "Jane")
        self.assertEqual(token.pos_, "PROPN")