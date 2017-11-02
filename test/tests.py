__author__ = 'kevin'
#!/usr/bin/python
'''
'''

import os
import sys
import shutil
import subprocess
from unittest import TestCase
from src.cooccurrence import *

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
    uw = ["i", "like", "dessert", "and", "I", "like", "Dessert", "Labs."]
    w = Words(iter(uw), 3)

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
        actual = cooccurrence(self.w, 'dessert', 'like')
        expected = 2
        self.assertEqual(actual, expected)
        actual = cooccurrence(self.w, 'dessert', 'labs')
        expected = 1
        self.assertEqual(actual, expected)
        actual = cooccurrence(self.w, 'labs', 'dessert')
        expected = 1
        self.assertEqual(actual, expected)


    def test_cooc_prob(self):
        actual = cooccurrence_prob(self.w, 'dessert', 'like')
        expected = 1.00
        self.assertEqual(actual, expected)
        actual = cooccurrence_prob(self.w, 'dessert', 'labs')
        expected = 0.50
        self.assertEqual(actual, expected)
        actual = cooccurrence_prob(self.w, 'labs', 'dessert')
        expected = 1.00
        self.assertEqual(actual, expected)


def readInput():
    with open('test/cat-in-the-hat.txt', 'r') as f:
        for line in f.readlines():
            for word in line.split():
                yield word

class CatInHat(TestCase):
    print(os.getcwd())

    w = Words(readInput(), 3)
    # print w.get_word_cnt('cat')

    def test_cooc_prob(self):
        actual = cooccurrence_prob(self.w, 'hat', 'cat')
        expected = 0.71
        self.assertEqual(actual, expected)
        actual = cooccurrence_prob(self.w, 'cat', 'hat')
        expected = 0.38
        self.assertEqual(actual, expected)
        actual = cooccurrence_prob(self.w, 'sit', 'sit')
        expected = 0.80
        self.assertEqual(actual, expected)
        actual = cooccurrence_prob(self.w, 'dessert', 'labs')
        expected = 0.00
        self.assertEqual(actual, expected)
