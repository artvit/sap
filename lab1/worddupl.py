import re


regex = re.compile(r'\b(\w+)\b[\s,.?!\'"]*')


def recursive_check_same_words(sentence: str):
    match = regex.search(sentence)
    if match:
        return sentence[match.end():].find(match.group(1)) > -1 or recursive_check_same_words(sentence[match.end():])
    else:
        return False
