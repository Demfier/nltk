# -*- coding: utf-8 -*-
"""
Tests for IBM Model 1 training methods
"""

import unittest

from collections import defaultdict
from nltk.align import AlignedSent
from nltk.align.ibm_model import AlignmentInfo
from nltk.align.ibm1 import IBMModel1


class TestIBMModel1(unittest.TestCase):
    def test_prob_t_a_given_s(self):
        # arrange
        src_sentence = ["ich", 'esse', 'ja', 'gern', 'räucherschinken']
        trg_sentence = ['i', 'love', 'to', 'eat', 'smoked', 'ham']
        corpus = [AlignedSent(trg_sentence, src_sentence)]
        alignment_info = AlignmentInfo((0, 1, 4, 0, 2, 5, 5),
                                       [None] + src_sentence,
                                       ['UNUSED'] + trg_sentence,
                                       None)

        translation_table = defaultdict(lambda: defaultdict(float))
        translation_table['i']['ich'] = 0.98
        translation_table['love']['gern'] = 0.98
        translation_table['to'][None] = 0.98
        translation_table['eat']['esse'] = 0.98
        translation_table['smoked']['räucherschinken'] = 0.98
        translation_table['ham']['räucherschinken'] = 0.98

        model1 = IBMModel1(corpus, 0)
        model1.translation_table = translation_table

        # act
        probability = model1.prob_t_a_given_s(alignment_info)

        # assert
        lexical_translation = 0.98 * 0.98 * 0.98 * 0.98 * 0.98 * 0.98
        expected_probability = lexical_translation
        self.assertEqual(round(probability, 4), round(expected_probability, 4))


if __name__ == '__main__':
    unittest.main()
