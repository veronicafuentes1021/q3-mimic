#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""
Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.

FOR CREATE_MIMIC_DICT
Returns a dict mapping each word to a list of words which follow it.
    For example:
        Input: "I am a software developer, and I don't care who knows"
        Output:
            {
                "" : ["I"],
                "I" : ["am", "don't"],
                "am": ["a"],
                "a": ["software"],
                "software" : ["developer,"],
                "developer," : ["and"],
                "and" : ["I"],
                "don't" : ["care"],
                "care" : ["who"],
                "who" : ["knows"]
            }
    PRINT MIMIC RANDOM
    Given a previously created mimic_dict and num_words,
    prints random words from mimic_dict as follows:
        - Use a start_word of '' (empty string)
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process num_words times
    """

__author__ = "Veronica Fuentes"


import random
import sys


def create_mimic_dict(filename):
    my_dict = {}
    with open(filename) as f:
        thing = f.read()
        text = thing.rstrip()
        words = text.split()
    i = 0
    my_dict[''] = [words[0]]
    for i in range(len(words) - 1):
        if words[i] not in my_dict:
            my_dict[words[i]] = [words[i + 1]]
        else:
            my_dict[words[i]].append(words[i+1])
        i += 1
    return my_dict


def print_mimic_random(mimic_dict, num_words):
    word = ''
    for n in range(num_words + 1):
        print(word, end=" ")
        if word not in mimic_dict:
            word = ''
        word = random.choice(mimic_dict[word])


def main(args):
    # Get input filename from command line args
    filename = args[0]

    # Create and print the jumbled (mimic) version of the input file
    print(f'Using {filename} as input:\n')
    d = create_mimic_dict(filename)
    print_mimic_random(d, 200)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
    else:
        main(sys.argv[1:])
    print('\n\nCompleted.')
