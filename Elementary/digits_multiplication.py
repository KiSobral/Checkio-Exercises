def checkio(number: int) -> int:
    res = 1

    while number > 0:
        if number % 10 != 0:
            res *= (number % 10)
        number = int(number/10)

    return res


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
