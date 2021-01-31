import numpy as np


def find_way_mul_helper(list_of_mul_input, array_matrix_attribute, level):
    if len(list_of_mul_input) != 1:
        print(list_of_mul_input)
        print(level)
        print("_____________________________")
    if level == 1:
        print(list_of_mul_input)
        print("_____________________________")
        return list_of_mul_input[0][2]

    else:

        list_of_mul = []

        for i in range(level - 1):

            item0_if_left = list_of_mul_input[i][0] + list_of_mul_input[i][1][0] * list_of_mul_input[i][1][1] * \
                            list_of_mul_input[i + 1][1][1]
            item0_if_right = list_of_mul_input[i + 1][0] + list_of_mul_input[i][1][0] * list_of_mul_input[i + 1][1][0] * \
                             list_of_mul_input[i + 1][1][1]

            if item0_if_right < item0_if_left:
                item0 = item0_if_right
                item2 = list_of_mul_input[i + 1][2] + [list_of_mul_input[i][2][-1]]
            else:
                item0 = item0_if_left
                item2 = list_of_mul_input[i][2] + [list_of_mul_input[i + 1][2][-1]]

            item1 = (list_of_mul_input[i][1][0], list_of_mul_input[i + 1][1][1])

            list_of_mul.append([item0, item1, item2])

        return find_way_mul_helper(list_of_mul, array_matrix_attribute, level - 1)


def find_way_mul(array_matrix_attribute):
    list_of_mul = []

    for i in range(len(array_matrix_attribute) - 1):
        list_of_mul.append(
            [array_matrix_attribute[i][0] * array_matrix_attribute[i][1] * array_matrix_attribute[i + 1][1]
                , (array_matrix_attribute[i][0], array_matrix_attribute[i + 1][1])
                , [i + 1]
             ])
    return find_way_mul_helper(list_of_mul, array_matrix_attribute, len(array_matrix_attribute) - 1)


def main():
    # number = int(input("please enter number of your matrix: " + "\n"))
    f = open("/home/mehdi/PycharmProjects/MultiMatrix/input", "r")
    number = int(f.readline())
    array_matrix = [np.matrix(f.readline()) for i in range(number)]
    f.close()
    size_of_array = len(array_matrix)
    array_matrix_attribute = [j.shape for j in array_matrix]
    regularity_of_multiple_of_matrix = find_way_mul(array_matrix_attribute)

    print(regularity_of_multiple_of_matrix)
    



if __name__ == '__main__':
    main()
