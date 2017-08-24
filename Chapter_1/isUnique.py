#!/usr/bin/env python
# date: 8/23/17
# name: Tony Hendrick
# description: Cracking the Coding Interview Chapter 1 - String

def isUnique(str):
    characters = set(str)
    if (len(characters) == len(str)):
        return 1
    return 0

#print(isUnique("abcdef"))

import string

def isPermutation(strOne, strTwo):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    for x in range(0, len(strOne)):
        letter_count[strOne[x]] += 1
    for x in range(0, len(strTwo)):
        letter_count[strTwo[x]] += 1
    for c in letter_count:
        if letter_count[c] == 1:
            return 0
    return 1

#print isPermutation("hello", "olleh")

def URLify(str):
    return str.replace(" ", "%20")

#print (URLify("Mr John Smith"))

import string
import collections

def palindromePermutation(str):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    letter_count[' '] = 0
    num_single = 0
    num_double = 0
    for x in range(0, len(str)):
        letter_count[str[x].lower()] += 1
    for c in letter_count:
        if letter_count[c] == 1 and c != ' ':
            num_single += 1
        elif letter_count[c] == 2:
            num_double += 1
    if (num_double == ((len(str) - 1) / 2) and num_single == 1):
        return 1
    return 0

#print (palindromePermutation("Racecar"))

import string

def oneAway(strOne, strTwo):
    letter_count = dict.fromkeys(string.ascii_lowercase, 0)
    sameChars = 0
    for x in range(0, len(strOne)):
        letter_count[strOne[x]] += 1
    for x in range(0, len(strTwo)):
        sameChars += letter_count[strTwo[x]]
    return sameChars == len(strOne) or sameChars == len(strOne) - 1 or sameChars == len(strOne) + 1

print (oneAway("pale", "bake"))




