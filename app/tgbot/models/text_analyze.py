from pydantic import BaseModel


class TextAnalysis(BaseModel):
    words_per_sentence: float
    sentences: int
    prepositions: int
    articles: int
    letters_per_sentence: float
    syllables_per_word: float
    letters_total: int
    printed_pages: int
    to_be_verbs: int
    words_between_pauses: float
    pauses_per_sentence: float
    max_sentence_length: int
    questions: int
    unique_words: int
    characters: int
    letters_per_word: float
    alphanumeric_characters: int
    paragraphs: int
    words_per_paragraph: list
    syllables_per_sentence: float
    syllables_total: int
    words_total: int
    pauses: int
    pronouns: int
    phrases: list[set]
    first_person: int
    second_person: int
    third_person: int
    most_used_letters: list
