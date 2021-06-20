def floaty(number):
    """
    Takes a number and prints and returns
    it as a floating point number
    :param number:
    :return:
    """
    try:
        float_number = float(number)
        print(float_number)
        return float_number
    except ValueError:
        print("Input value unable to be converted to float")


x = floaty(input("Give me a number? "))
