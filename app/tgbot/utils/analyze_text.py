import re
from collections import Counter


def count_words(text, word_list):
    """Count the number of times the words in word_list appear in the text."""
    return sum([text.lower().count(word) for word in word_list])


def count_syllables(word):
    """Count the number of syllables in a word."""
    # based on the algorithm from the Natural Language Toolkit (NLTK)
    vowels = 'aeiouy'
    num_vowels = len([c for c in word if c in vowels])
    if num_vowels == 0:
        return 1
    else:
        return num_vowels - word.count('e') - (1 if word[-2:] == 'es' and word[-3] not in vowels else 0) - (
            1 if word[-1] == 'e' and word[-2] not in vowels and word[-3:] != 'the' else 0)


def make_analysis(text):
    # split the text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    num_sentences = len(sentences)

    # calculate words per sentence, letters per sentence, syllables per sentence, and pauses per sentence
    words_per_sentence = []
    letters_per_sentence = []
    syllables_per_sentence = []
    pauses_per_sentence = []
    for sentence in sentences:
        # count the number of words in the sentence
        words = sentence.split()
        num_words = len(words)
        words_per_sentence.append(num_words)

        # count the number of letters in the sentence (excluding spaces and punctuation)
        letters = [c for c in sentence if c.isalnum()]
        num_letters = len(letters)
        letters_per_sentence.append(num_letters)

        # count the number of syllables in the sentence
        num_syllables = sum([count_syllables(word) for word in words])
        syllables_per_sentence.append(num_syllables)

        # count the number of pauses in the sentence (i.e. commas, semicolons, and colons)
        num_pauses = sentence.count(',') + sentence.count(';') + sentence.count(':')
        pauses_per_sentence.append(num_pauses)

    # calculate other parameters
    prepositions = count_words(text,
                               ['about', 'above', 'across', 'after', 'against', 'along', 'among', 'around',
                                'at', 'before', 'behind', 'below', 'beneath', 'beside', 'between', 'beyond',
                                'but', 'by', 'despite', 'down', 'during', 'except', 'for', 'from', 'in',
                                'inside', 'into', 'like', 'near', 'of', 'off', 'on', 'onto', 'out', 'outside',
                                'over', 'past', 'since', 'through', 'throughout', 'to', 'toward', 'under',
                                'underneath', 'until', 'up', 'upon', 'with', 'within', 'without'])
    articles = count_words(text, ['a', 'an', 'the'])
    to_be_verbs = count_words(text, ['am', 'is', 'are', 'was', 'were', 'be', 'been', 'being'])
    questions = len(re.findall(r'\?', text))
    unique_words = len(set(re.findall(r'\b\w+\b', text)))
    characters = len(text)
    alphanumeric_characters = len(re.findall(r'[a-zA-Z0-9]', text))
    max_sentence_length = max(words_per_sentence)
    try:
        words_between_pauses = sum(words_per_sentence) / sum(pauses_per_sentence)
    except ZeroDivisionError:
        words_between_pauses = 0
    pronouns = count_words(text, ['I', 'you', 'he', 'she', 'it', 'we', 'they'])
    paragraphs = text.count('\n\n') + 1
    words_per_paragraph = [len(paragraph.split()) for paragraph in text.split('\n\n')]
    syllables_per_word = sum(syllables_per_sentence) / sum(words_per_sentence)
    syllables_total = sum(syllables_per_sentence)
    words_total = sum(words_per_sentence)
    letters_per_word = sum(letters_per_sentence) / sum(words_per_sentence)
    pauses = sum(pauses_per_sentence)
    phrases = Counter(re.findall(r'\b[\w\s]+\b', text)).most_common(10)
    first_person = count_words(text, ['I', 'we'])
    second_person = count_words(text, ['you'])
    third_person = count_words(text, ['he', 'she', 'it', 'they'])
    # calculate most used letters
    letters = {}
    for c in text:
        if c.isalpha():
            c_lower = c.lower()
            if c_lower not in letters:
                letters[c_lower] = 1
            else:
                letters[c_lower] += 1
    most_used_letters = sorted(letters.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        'words_per_sentence': sum(words_per_sentence) / num_sentences,
        'sentences': num_sentences,
        'prepositions': prepositions,
        'articles': articles,
        'letters_per_sentence': round(sum(letters_per_sentence) / num_sentences, 2),
        'syllables_per_word': round(syllables_per_word, 2),
        'letters_total': characters,
        'printed_pages': 0,  # this requires additional information
        'to_be_verbs': to_be_verbs,
        'words_between_pauses': words_between_pauses,
        'pauses_per_sentence': sum(pauses_per_sentence) / num_sentences,
        'max_sentence_length': max_sentence_length,
        'questions': questions,
        'unique_words': unique_words,
        'characters': characters,
        'letters_per_word': round(letters_per_word, 2),
        'alphanumeric_characters': alphanumeric_characters,
        'paragraphs': paragraphs,
        'words_per_paragraph': words_per_paragraph,
        'syllables_per_sentence': round(sum(syllables_per_sentence) / num_sentences, 2),
        'syllables_total': syllables_total,
        'words_total': words_total,
        'pauses': pauses,
        'pronouns': pronouns,
        'phrases': phrases,
        'first_person': first_person,
        'second_person': second_person,
        'third_person': third_person,
        'most_used_letters': most_used_letters
    }
