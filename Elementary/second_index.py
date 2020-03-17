def second_index(text: str, symbol: str) -> [int, None]:
    if text.count(symbol) < 2:
        return None

    x = text.find(symbol) + 1
    split = text[x:]

    return split.find(symbol) + x


if __name__ == '__main__':
    print('Example:')
    print(second_index("sims", "s"))

    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
