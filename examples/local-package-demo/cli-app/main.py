from wordcount import word_count
# from wordcount.counter import word_count,


def main():
    samples = [
        "The quick brown fox",
        "  hello   world  ",
        "",
    ]
    for text in samples:
        print(f"{word_count(text):>3} words | {repr(text)}")


if __name__ == "__main__":
    main()
