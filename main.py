def get_book_as_string(book_name):
    with open("books/" + book_name + ".txt") as f:
        file_contents = f.read()

    return file_contents


def count_words(content):
    return len(content.split())


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
    print("--- Begin report of books/frankenstein.txt ---")

    total_words = count_words(content)
    print(f"{total_words} words found in the document")

    charcter_counts = count_characters(content)
    for character, count in charcter_counts.items():
        if not character.isalpha():
            continue

        print(f"The '{character}' was found {count} times")

    print("--- End Report ---")


def main():
    frankenstein_book = get_book_as_string("frankenstein")

    # print(count_words(frankenstein_book))
    # print(count_characters(frankenstein_book))
    print_report(frankenstein_book)


if __name__ == "__main__":
    main()
