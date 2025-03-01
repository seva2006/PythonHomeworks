import string
from collections import Counter

def word_frequency_counter():
    try:
        with open("sample.txt", "r") as file:
            text = file.read()
    except FileNotFoundError:
        print("The file 'sample.txt' does not exist.")
        print("Please type a paragraph to create the file:")
        text = input()

        with open("sample.txt", "w") as file:
            file.write(text)

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    word_counts = Counter(words)

    total_words = len(words)

    top_5_words = word_counts.most_common(5)

    print(f"Total words: {total_words}")
    print("Top 5 most common words:")
    for word, count in top_5_words:
        print(f"{word} - {count} times")

    with open("word_count_report.txt", "w") as report_file:
        report_file.write("Word Count Report\n")
        report_file.write(f"Total Words: {total_words}\n")
        report_file.write("Top 5 Words:\n")
        for word, count in top_5_words:
            report_file.write(f"{word} - {count}\n")

word_frequency_counter()
