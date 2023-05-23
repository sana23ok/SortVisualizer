

def convert(int_array):
    return [str(element) for element in int_array]


def saveInTxtFile(array, name):
    with open(name + '.txt', 'w') as file:
        elements_per_line = 20
        elements = convert(array)

        for i in range(0, len(elements), elements_per_line):
            line = ', '.join(map(str, elements[i:i + elements_per_line])) + '\n'
            file.write(line)

