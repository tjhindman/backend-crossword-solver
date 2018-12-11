#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "tjhindman"

import re

# YOUR HELPER FUNCTION GOES HERE


def xword_sol(word, dic):
    in_word = word.replace(" ", ".")
    re_word = re.compile(in_word)

    for w in dic:
        if len(word) == len(w) and re.match(re_word, w):
            print w


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()

    # YOUR ADDITIONAL CODE HERE
    xword_sol(test_word, words)


if __name__ == '__main__':
    main()
