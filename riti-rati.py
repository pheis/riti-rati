import xml.etree.ElementTree as ET
from itertools import permutations

WORD_LIST_FILE = "kotus-sanalista_v1/kotus-sanalista_v1.xml"


def read_words_to_set(word_list_file_name):
    xml_tree = ET.parse(word_list_file_name)
    return {child[0].text for child in xml_tree.getroot()}


def generate_words(letters, extra_letters):
    word_set = set()
    for l in extra_letters:
        all_letters = letters + l
        for i in range(2, len(all_letters) + 1):
            for w in permutations(all_letters, i):
                word_set.add("".join(w))
    return word_set


if __name__ == "__main__":
    real_words = read_words_to_set(WORD_LIST_FILE)

    letters = "rnteafm"
    extra_letters = "a"

    jumble_words = generate_words(letters, extra_letters)
    answer_words = jumble_words.intersection(real_words)

    for word in answer_words:
        print(word)
