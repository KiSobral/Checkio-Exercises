def checkio(number: int) -> str:
    res = ""

    if number % 3 == 0:
        res += "Fizz"

    if number % 5 == 0:
        if len(res) > 0:
            res += " "

        res += "Buzz"

    if len(res) == 0:
        res = str(number)

    return res


if __name__ == '__main__':
    print('Example:')
    print(checkio(15))

    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"
