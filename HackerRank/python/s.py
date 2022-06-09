def find_duplicates(array):
    duplicates = set()
    for i, el in enumerate(array):
        for a in array[i+1:]:
            if el == a:
                duplicates.add(el)
    return list(duplicates)


def run_test(subject, expected):
    returned = find_duplicates(subject)
    result = (returned == expected)

    print(f"Caso de teste: {subject}")
    print(f"Esperado: {expected}")
    print(f"Retornado: {returned}")
    print(f"Resultado: {'Sucesso' if result else 'Falha'}\n")

if __name__ == '__main__':

    subject_1 = [1, 2, 3, 4]
    expected_1 = []
    run_test(subject_1, expected_1)

    subject_2 = [1, 2, 2, 3, 4]
    expected_2 = [2]
    run_test(subject_2, expected_2)

    subject_3 = [1, 2, 2, 3, 4, 4]
    expected_3 = [2, 4]
    run_test(subject_3, expected_3)

    subject_4 = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5]
    expected_4 = [2, 4, 5]
    run_test(subject_4, expected_4)

    subject_5 = [1, 2, 4, 2, 3, 4, 5, 4, 5, 5, 5, 5, 5, 5, 5]
    expected_5 = [2, 4, 5]
    run_test(subject_5, expected_5)
