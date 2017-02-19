__author__ = 'kevin'
#!/usr/bin/python
'''
'''

import os
import sys
import shutil
import subprocess
from unittest import TestCase
from src.program import *

SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

__author__ = 'kevin'


class Test1(TestCase):
    def test_1(self):
        actual = count_words(Words(["word", 'word', 'no']), 'word')
        expected = 2
        self.assertEqual(actual, expected)

        actual = count_words(Words(['no']), 'word')
        expected = 0
        self.assertEqual(actual, expected)

        actual = count_words(Words(["w", 'word', 'no']), 'word')
        expected = 1
        self.assertEqual(actual, expected)

class Dessert(TestCase):
    uw = ["i", "like", "dessert", "and", "I", "like", "Dessert", "Labs"]
    w = Words(format_words(uw))

    def test_1(self):
        actual = count_words(self.w, 'word')
        expected = 0
        self.assertEqual(actual, expected)
        actual = count_words(self.w, 'I')
        expected = 2
        self.assertEqual(actual, expected)
        actual = count_words(self.w, 'i')
        expected = 2
        self.assertEqual(actual, expected)
        actual = count_words(self.w, 'dessert')
        expected = 2
        self.assertEqual(actual, expected)
        actual = count_words(self.w, 'labs')
        expected = 1
        self.assertEqual(actual, expected)

    def test_cooc(self):
        actual = cooccurrence(self.w, 'dessert', 'like', 3)
        expected = 2
        self.assertEqual(actual, expected)
        actual = cooccurrence(self.w, 'dessert', 'labs', 3)
        expected = 1
        self.assertEqual(actual, expected)
        actual = cooccurrence(self.w, 'labs', 'dessert', 3)
        expected = 1
        self.assertEqual(actual, expected)



