
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    checkArgs(height, weight)

    bmiList = []
    for h, w in zip(height, weight):
        bmiList.append(w/(h * h))
    return (bmiList)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    res = []
    for item in bmi:
        if (item > limit):
            res.append(True)
        else:
            res.append(False)
    return (res)


def checkArgs(height, weight) -> int:
    if (len(height) != len(weight)):
        raise ValueError("Length are not the same.")
    for x in height:
        if ((isinstance(x, int) or isinstance(x, float)) and not isinstance(x, bool)):
            continue
        else:
            raise ValueError("Error, not a list of int or float.")
    for y in weight:
        if (isinstance(x, int) or isinstance(x, float)):
            continue
        else:
            raise ValueError("Error, not a list of int or float.")


def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)

    try:
        height = [2.71, 1.15, "Hello"]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)

    try:
        height = [2.71, 1.15, "Hello"]
        weight = [165.3, 38.4]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)

    try:
        height = [2.71, 1.15, True]
        weight = [165.3, 38.4, 0]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)

    try:
        height = [2.71, 1.15]
        weight = [165.3, 3]

        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)


if (__name__ == "__main__"):
    main()
