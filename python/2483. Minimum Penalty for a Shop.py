def bestClosingTime(customers: str) -> int:
    pen = 0
    ans = 0
    minPen = 0
    for i, c in enumerate(customers):
        if c == "Y":
            pen -= 1
        else:
            pen += 1
        if pen < minPen:
            minPen = pen
            ans = i +1
    return ans

if __name__ == "__main__":
    print("expected 0 |",bestClosingTime(customers = "NNNNN"))
    print("expected 0 |",bestClosingTime(customers = "NNNYNN"))
    print("expected 1 |",bestClosingTime(customers = "Y"))
    print("expected 2 |",bestClosingTime(customers = "YYNY"))
    print("expected 4 |",bestClosingTime(customers = "YYYY"))