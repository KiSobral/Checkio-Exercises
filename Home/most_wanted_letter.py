def checkio(text: str) -> str:
    text = ''.join(filter(str.isalpha, text)).lower()
    dic = {}

    for letter in text:
        dic[letter] = text.count(letter)

    return sorted(list(dic.items()), key=lambda x: (-x[1], x[0]))[0][0]


if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
