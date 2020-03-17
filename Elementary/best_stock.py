def best_stock(a):
    res_key = ""
    res_value = 0.0

    for k, v in a.items():
        if v > res_value:
            res_key = k
            res_value = v

    return res_key


if __name__ == '__main__':
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI"
