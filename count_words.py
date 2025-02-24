def count_words_in_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        print("Файл не знайдено.")
        return 0
word_count = count_words_in_file("quote.txt")
print(f"Кількість слів у файлі: {word_count}")
