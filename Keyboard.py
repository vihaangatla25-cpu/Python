"""
Keyboard Predictor (complete solution)
Python 3, standard library only. Keep this file in the same folder as the books folder.

Your phone's keyboard guesses your next word. Here we build one that
learns from a whole book, then compare two very different authors:
    books/alice.txt     Alice's Adventures in Wonderland (Lewis Carroll, 1865)
    books/sherlock.txt  The Adventures of Sherlock Holmes (Arthur Conan Doyle, 1892)
Both are public domain, from Project Gutenberg.
"""
import random
from collections import Counter, defaultdict
from pathlib import Path

BOOKS = {"alice": "books/alice.txt", "sherlock": "books/sherlock.txt"}
USE_TRIGRAMS = True     # Final mission: look at the last TWO words, not just one


# ------------------------------------------------------
# step o (given): turn a book into a clean list of words
# ------------------------------------------------------
def load_words (path):
    text = (Path(_file_).parent / path).read_text(encoding="utf-8").lower()
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    chars = [ch if ch.isalpha() or ch == else for ch in text]
    words = []
    for word in "".join(chars).split():
        word = word.strip("'")          # 'hello' -> hello, but keep don't
        if word:
            words.append(word)
    return words


# ----------------------------------------------------------------
# Step 1: Count which word comes after which (bigrams)
#   "the cat sat" -> after "the": {cat: 1}, after "cat": {sat: 1}
# ----------------------------------------------------------------
def build_bigrams (words):
    model = defaultdict (Counter)
    for current, following in zip(words, words [1:]):
        model [current] [following] += 1
    return model


# Final mission: the same idea, but the key is the last TWO words
def build_trigrams (words):
    model defaultdict(Counter)
    for a, b, c in zip(words, words [1:], words [2:]):
        model[(a, b)][c] += 1
    return model


def build_model (words):
    return {
        "unigrams": Counter (words),
        "bigrams": build_bigrams (words),
        "trigrams": build_trigrams (words),
    }


# ----------------------------------------------------------------
# Step 2: Suggest the top k next words, with probailities
#   probability = times this word followed / times anything followed 
# ----------------------------------------------------------------
def top_k(counter, k):
    total = sum(counter.values())
    return [(word, count / total) for word, count in counter.most_common(k)]


def suggest(model, typed, k=3):
    """typed = list of words so far. Returns [(word, probability), ...]."""
    if USE_TRIGRAMS and len(typed) >= 2:
        key = (typed[-2], typed[-1])
        if key in model ["trigrams"]:
            return top_k(model["trigrams"] [key], k)
    if typed and typed [-1] in model ["bigrams"]: 
        return top_k(model ["bigrams"] [typed[-1]], k)

    # "Backoff": never seen this word, so suggest the most common words overall 
    return top_k(model ["unigrams"], k)


# ----------------------------------------------------------------
# Step 3: Let the model write on its own
#   greedy always pick the top word, random = pick by probability
# ----------------------------------------------------------------
def generate(model, start, length=15, mode="random"):
    