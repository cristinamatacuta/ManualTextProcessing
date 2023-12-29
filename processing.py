import re
import sys


def read_book(file_path):
    """Read the content of a text file.

    Args:
        file_path (str): The path to the text file.

    Returns:
        str: The content of the text file.

    Raises:
        FileNotFoundError: If the file is not found.
    """
    try:
        with open(file_path, "r") as text_file:
            return text_file.read()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        sys.exit(1)


def read_stop_words():
    """Read and return the stop words from the specified file.

    Returns:
        list: List of stop words.
    """
    with open("stopwordlist.txt", "r") as file_read2:
        stop_words = [line.strip() for line in file_read2.readlines()]
        return stop_words


def get_sentences(text):
    """Split the input text into sentences using regular expressions.

    Args:
        text (str): The input text.

    Returns:
        list: List of sentences.
    """
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return sentences


def get_words(text):
    """Tokenize the input text and remove punctuation.

    Args:
        text (str): The input text.

    Returns:
        list: List of words.
    """
    sentences = get_sentences(text)
    words = []
    for sentence in sentences:
        sentence_words = re.findall(r"\b\w+(?:[-]\w+)*\b", sentence)
        words.extend(sentence_words)
    return words


def count_words(sentence):
    """Count the number of words in a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        int: Number of words in the sentence.
    """
    words = get_words(sentence)
    return len(words)


def longest_sentence(text):
    """Find and return the longest sentence in the text.

    Args:
        text (str): The input text.

    Returns:
        str: The longest sentence in the text.
    """
    sentences = get_sentences(text)
    sentences.sort(key=count_words, reverse=True)
    longest_sentence_in_text = sentences[0]
    return longest_sentence_in_text


def longest_word(text):
    """Find and return the longest word in the text.

    Args:
        text (str): The input text.

    Returns:
        str: The longest word in the text.
    """
    words = get_words(text)
    words.sort(key=len, reverse=True)
    longest_word_in_text = words[0]
    return longest_word_in_text


def stop_words_removed(text):
    """Remove stop words from the input text.

    Args:
        text (str): The input text.

    Returns:
        list: List of words with stop words removed.
    """
    stop_words = read_stop_words()
    words = get_words(text)
    clean_words = [word for word in words if word.lower() not in stop_words]
    return clean_words


def named_entities_a_l(text):
    """Extract and return named entities from A to L in the input text.

    Args:
        text (str): The input text.

    Returns:
        list: List of named entities from A to L.
    """
    stop_words = read_stop_words()
    pattern = r"(?<!\n\n)(?<![.!?]\s)[A-L][a-z]\w*(?: [A-Z][a-z]\w*)*"
    matches = [
        match for match in re.findall(pattern, text) if match.lower() not in stop_words
    ]
    matches_set = set(matches)
    matches_lst = list(matches_set)
    matches_lst.sort()
    return matches_lst


def named_entities_m_z(text):
    """Extract and return named entities from M to Z in the input text.

    Args:
        text (str): The input text.

    Returns:
        list: List of named entities from M to Z.
    """
    stop_words = read_stop_words()
    pattern = r"(?<!\n\n)(?<![.!?]\s)[M-Z][a-z]\w*(?: [A-Z][a-z]\w*)*"
    matches = [
        match for match in re.findall(pattern, text) if match.lower() not in stop_words
    ]
    matches_set = set(matches)
    matches_lst = list(matches_set)
    matches_lst.sort()
    return matches_lst


def ten_most_used_words(text):
    """Print the top 10 most used words in the input text.

    Args:
        text (str): The input text.
    """
    words = stop_words_removed(text)
    word_frequency = {}
    for word in words:
        word_lower = word.lower()
        if word_lower in word_frequency:
            word_frequency[word_lower] += 1
        else:
            word_frequency[word_lower] = 1
    word_frequency_order = sorted(
        word_frequency.items(), key=lambda x: x[1], reverse=True
    )
    top_ten_words = dict(word_frequency_order[:10])
    for key, value in top_ten_words.items():
        print(key + " : " + str(value))


def main():
    """Main function to process and analyze the book chapter text."""
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    text = read_book(input_file_path)

    # Aesthetics space
    print("\n" * 3)

    # Longest sentence in the text
    longest_sentence_in_text = longest_sentence(text)
    print("The longest sentence in the text is: \n")

