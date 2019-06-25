def calculate_rectangular_area(side1, side2):
    """
    Calculates rectangular area.
    :param side1: integer, greater than zero
    :param side2: integer, greater than zero
    :return: area based on multiplication of sides
    """
    return side1 * side2


def calculate_square_area(side):
    return side ** 2


if __name__ == '__main__':
    # kod uruchomi się tylko gdy zostanie uruchomiony ten plik
    # nie uruchomi się gdy zostanie zaimportowany w innym module
    rect_result = calculate_rectangular_area(14, 98)
    print(rect_result)
