import xml.etree.ElementTree as ET
from itertools import permutations


def read_words_to_set(word_list_file_name):
    xml_tree = ET.parse(word_list_file_name)
    return {child[0].text for child in xml_tree.getroot()}


def generate_words(letters):
    word_set = set()
    for i in range(2, len(letters) + 1):
        for w in permutations(letters, i):
            word_set.add("".join(w))
    return word_set


if __name__ == "__main__":
    word_list_file = "kotus-sanalista_v1/kotus-sanalista_v1.xml"
    real_words = read_words_to_set(word_list_file)

    letters = "gteeöeb" + "i"
    jumble_words = generate_words(letters)

    answer_words = jumble_words.intersection(real_words)

    for word in answer_words:
        print(word)
