import sys

from stats import count_words


def get_book_as_string(book_path):
    with open(book_path) as f:
        file_contents = f.read()

    return file_contents


def count_characters(content):
    content = content.strip()
    character_counts = {}

    for character in content:
        character = character.lower()
        if character not in character_counts:
            character_counts[character] = 0

        character_counts[character] += 1

    return character_counts


def print_report(content):
    print("--- Begin report of books ---")

    total_words = count_words(content)
    print(f"{total_words} words found in the document")

    charcter_counts = count_characters(content)
    for character, count in charcter_counts.items():
        if not character.isalpha():
            continue

        print(f"The '{character}' was found {count} times")

    print("--- End Report ---")


def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_as_string(sys.argv[1])

    # print(count_words(frankenstein_book))
    # print(count_characters(frankenstein_book))
    print_report(book)


if __name__ == "__main__":
    main()
